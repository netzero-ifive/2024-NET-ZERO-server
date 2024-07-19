from .settings import AWS_STORAGE_BUCKET_NAME, S3_HOST_NAME


def get_resized_image_url(image_path: str):
    resized_path = (
        f"https://{AWS_STORAGE_BUCKET_NAME}{S3_HOST_NAME}/resize/{image_path}"
    )
    return resized_path
