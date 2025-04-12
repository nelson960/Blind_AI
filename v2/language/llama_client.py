import requests

class LLaMAClient:
    def __init__(self, model="llama2"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def generate_description(self, yolo_objs, blip_caption=""):
        object_list = ", ".join(yolo_objs)

        prompt = (
            "You are a helpful assistant describing the scene to a blind person. "
            "Speak clearly and politely, in a calm and human tone. "
            "Do not introduce yourself. Do not start with phrases like 'Sure' or 'Let me describe...'. "
            "Start directly and naturally with the scene description.\n\n"

            "Use spatial terms like 'to your left', 'on the right', or 'in front of you'. "
            "Base your description only on the following detected objects:\n"
            f"{object_list}\n\n"
        )

        if blip_caption:
            prompt += (
                f"You may optionally use this image caption *only if* it aligns with the object list:\n"
                f"\"{blip_caption}\"\n\n"
            )

        prompt += (
            "Do not make anything up. Do not guess or imagine extra details. "
            "Do not include fictional actions, emotions, or interactions. "
            "Do not use emojis, roleplay, or express feelings. "
            "Do not refer to yourself, and do not mention being an AI.\n"
            "Do not ask the user any follow-up questions — end your response naturally after the description.\n\n"
            "Just describe the visible scene in simple, helpful, spatially-aware language."
        )

        response = requests.post(self.url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json()["response"].strip()
