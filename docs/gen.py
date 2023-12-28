import os
import yaml

def generate_yaml(directory):
    yaml_data = []
    for root, dirs, files in os.walk(directory):
        relative_path = os.path.relpath(root, directory)
        paths = []
        readme_file = None

        for i, file in enumerate(files):
            file_path = os.path.join(relative_path, file)
            if file.lower() == 'readme.md':
                readme_file = {'path': file_path}
            else:
                paths.append({'path': file_path})

        if readme_file:
            yaml_data.append({'path': readme_file['path'], 'sections': paths})
        elif paths:
            yaml_data.append({'path': paths[0]['path'], 'sections': paths[1:]})

    return yaml_data

def save_yaml(data, output_file):
    with open(output_file, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)

# Example usage
directory_path = './en'
output_file_path = 'tmp.yml'

yaml_data = generate_yaml(directory_path)
save_yaml(yaml_data, output_file_path)