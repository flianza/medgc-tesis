import torchvision.transforms as T
from common.vision.transforms import ResizeImage


def get_data_transform(
    random_horizontal_flip=False,
    random_color_jitter=False,
    resize_size=28,
    norm_mean=0.5,
    norm_std=0.5,
):
    transforms = [ResizeImage(resize_size)]

    if random_horizontal_flip:
        transforms.append(T.RandomHorizontalFlip())
    if random_color_jitter:
        transforms.append(T.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5))

    transforms.extend(
        [
            T.Resize(32),
            T.ToTensor(),
            T.Lambda(lambda x: x.repeat(3, 1, 1)),
            T.Normalize(mean=norm_mean, std=norm_std),
        ]
    )

    return T.Compose(transforms)
