{
  "nodes": [
    {
      "id": "webhook",
      "name": "Receive Video URL",
      "type": "n8n-nodes-base.webhook",
      "position": [200, 300],
      "parameters": {
        "path": "analyze-accent",
        "httpMethod": "POST",
        "responseMode": "onReceived"
      }
    },
    {
      "id": "downloadVideo",
      "name": "Download Video",
      "type": "n8n-nodes-base.httpRequest",
      "position": [400, 300],
      "parameters": {
        "url": "={{ $json[\"body\"][\"videoUrl\"] }}",
        "responseFormat": "file",
        "output": "data",
        "dataPropertyName": "videoFile"
      }
    },
    {
      "id": "extractAudio",
      "name": "Extract Audio",
      "type": "n8n-nodes-base.executeCommand",
      "position": [600, 300],
      "parameters": {
        "command": "ffmpeg -i video.mp4 -vn -ar 16000 -ac 1 -f wav audio.wav"
      }
    },
    {
      "id": "transcribe",
      "name": "Transcribe Audio",
      "type": "n8n-nodes-base.httpRequest",
      "position": [800, 300],
      "parameters": {
        "url": "https://api.openai.com/v1/audio/transcriptions",
        "method": "POST",
        "authentication": "predefinedCredentialType",
        "sendBinaryData": true,
        "binaryPropertyName": "audio.wav",
        "headerParameters": {
          "Authorization": "Bearer YOUR_OPENAI_AP
