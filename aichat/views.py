from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.conf import settings
from .models import ChatMessage
import json
import requests


@login_required
def camploy_ai_chat_view(request):
    """Page du chat IA avec historique"""
    messages = ChatMessage.objects.filter(user=request.user)
    conversation_history = [
        {'content': msg.message, 'sender': msg.role, 'time': msg.created_at.strftime('%H:%M')}
        for msg in messages
    ]
    return render(request, "camploy_ai_chat.html", {'conversation_history': conversation_history})


@login_required
@require_POST
def camploy_ai_chat_api(request):
    """API backend qui sauvegarde les messages et envoie à DeepSeek"""
    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        return JsonResponse({"success": False, "error": "JSON invalide"}, status=400)

    user_message = data.get("message", "").strip()
    conversation_history = data.get("conversation_history", [])

    if not user_message:
        return JsonResponse({"success": False, "error": "Message vide"}, status=400)

    # Sauvegarde du message utilisateur
    ChatMessage.objects.create(user=request.user, role='user', message=user_message)

    # Prompt système (raccourci — adapte si besoin)
    system_prompt = (
        "Tu es Camploy AI, assistant intelligent spécialisé dans l'aide à la recherche d'emploi "
        "et l'optimisation de carrière..."
    )

    # Construire l'historique pour l'IA
    messages_for_ai = [{"role": "system", "content": system_prompt}]
    for msg in conversation_history[-10:]:
        role = "user" if msg.get('sender') == 'user' else "assistant"
        messages_for_ai.append({"role": role, "content": msg.get('content', '')})
    messages_for_ai.append({"role": "user", "content": user_message})

    # Appel API DeepSeek (gère les erreurs réseau)
    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek-chat",
                "messages": messages_for_ai,
                "max_tokens": 500,
                "temperature": 0.7,
            },
            timeout=30,
        )
    except requests.exceptions.RequestException:
        return JsonResponse({"success": False, "error": "Erreur connexion à DeepSeek"}, status=502)

    if response.status_code == 200:
        ai_response = response.json()
        ai_message = ai_response.get("choices", [{}])[0].get("message", {}).get("content", "")
        ChatMessage.objects.create(user=request.user, role='ai', message=ai_message)
        return JsonResponse({"success": True, "response": ai_message})
    else:
        return JsonResponse({"success": False, "error": "Erreur avec l'API DeepSeek"}, status=502)


# @login_required
# @require_POST
# def clear_chat(request):
#     """Effacer toute la conversation d’un utilisateur"""
#     ChatMessage.objects.filter(user=request.user).delete()
#     return JsonResponse({"success": True})
