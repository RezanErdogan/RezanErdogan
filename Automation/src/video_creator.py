from moviepy.editor import TextClip, CompositeVideoClip, ImageClip
import logging

def create_video(text, background_image_path):
    try:
        text_clip = TextClip(text, fontsize=24, color='white')
        background_clip = ImageClip(background_image_path, duration=text_clip.duration)

        final_clip = CompositeVideoClip([background_clip, text_clip.set_pos("center")])
        video_path = "output_video.mp4"
        final_clip.write_videofile(video_path, codec='libx264', audio_codec='aac')
        return video_path
    except Exception as e:
        logging.error(f"Fehler bei der Videoerstellung: {e}")
        return None