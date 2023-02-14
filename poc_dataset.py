from pathlib import Path

from PIL import Image

def generate_dataset(split):
    file_names = []
    json_path = Path(__file__).parent.absolute()
    if split == 'train':
        json_path /= 'train_seg.json'
        for path in Path('dataset-1').iterdir():
            file_names.append(str(path))
        for path in Path('dataset-2').iterdir():
            file_names.append(str(path))
    elif split == 'val':
        json_path /= 'val_seg.json'
        for path in Path('dataset-3').iterdir():
            file_names.append(str(path))
    else:
        raise NotImplementedError(f'{split} should be train or val')

    items = []
    for file_name in file_names:
        item = {}
        item['file_name'] = filename
        image = Image.open(file_name)
        width, height = image.size
        item['width'] = width
        item['height'] = height
        item['image_id'] = filename

        label_directory = Path(file_name).parent.with_name('labels')
        name = Path(file_name).name
        item['sem_seg_file_name'] = label_directory / name

        items.append(item)

    with open(json_path, 'w') as json_file:
        json.dump(items, json_file)


def train_dataset_function():
    json_path = Path(__file__).parent.absolute() / 'train_seg.json'
    if not json_path.exists():
        generate_dataset('train')
    return json.load(open(json_path))

def val_dataset_function():
    json_path = Path(__file__).parent.absolute() / 'val_seg.json'
    if not json_path.exists():
        generate_dataset('val')
    return json.load(open(json_path))
