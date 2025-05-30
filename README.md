# English Accent Analyzer – Quick Guide for HR
# Purpose
This tool helps evaluate a people’s spoken English by analyzing their accent and fluency from a short video. 


# What the Tool Does
Takes a video URL (e.g., from Loom, Google Drive, Dropbox, or any public host)

Extracts the audio from the video

Transcribes the speech using OpenAI’s Whisper AI

Analyzes the transcript for accent clues

# Returns:

Detected accent (e.g., American, British)

Confidence score

Short explanation

Transcript excerpt

# Step 1: Prepare the Video Link
Make sure the candidate’s video is:

Publicly accessible (no login required)

In a supported format like .mp4 or .webm

Hosted on any service that allows direct access to the file

# Example:

arduino
Copy
Edit
https://example.com/interview-video.mp4
# Avoid:

YouTube links without converting to direct video

Password-protected or private sharing links

# Step 2: Send the Video to the Analyzer
Use a simple form or tool (like Postman or internal software) to send a POST request to the analyzer with this body:

json
Copy
Edit
{
 "videoUrl": "https://example.com/interview-video.mp4"
}
The technical team will provide you with a permanent analyzer URL to submit links to (e.g., https://internal.company.com/webhook/analyze-accent).

# Step 3: Review the Result
The system will return an analysis that includes:

json
Copy
Edit
{
  "Accent": "British",
  "Confidence": "80",
  "Explanation": "Common British terms used.",
  "Transcript": "Hi there, I’m applying for the marketing role..."
}
This gives you a quick summary of:

Which accent was detected

How confident the system is

A sample of the candidate’s speech
