from .settings import AWS_STORAGE_BUCKET_NAME, S3_HOST_NAME
import os


def get_resized_image_url(image_path: str):
    # 파일 이름과 확장자 분리
    base_name, _ = os.path.splitext(image_path)

    # 새로운 파일 경로 생성 (확장자를 .webp로 변경)
    new_image_path = f"{base_name}.webp"

    resized_path = (
        f"https://{AWS_STORAGE_BUCKET_NAME}{S3_HOST_NAME}/resize/{new_image_path}"
    )
    return resized_path


def format_distance(distance):
    if distance is None:
        return None
    if distance < 1000:
        return f"{int(distance)}m"
    else:
        return f"{distance/1000:.1f}km"
