from importlib import metadata
print(metadata.version("pip"))
# print(metadata.metadata('pip'))
print(list(metadata.metadata('pip')))
print(metadata.metadata('pip')['Home-page'])
print(len(metadata.files('pip')))
# print([p for p in metadata.files('pip') if p.suffix == '.py'])
init_path = [p for p in metadata.files('pip') if p.suffix == '.py'][0]
# print(init_path.read_text())
print(metadata.requires('requests'))
