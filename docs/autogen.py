import material_sphinx
import pathlib
import shutil

PAGES = {
    "sourcecode.md": [
        "lightning_pod.network.model.Encoder",
        "lightning_pod.network.model.Decoder",
        "lightning_pod.network.model.LitModel",
    ]
}

root_dir = pathlib.Path(__file__).resolve().parents[1]


def generate(dest_dir):
    doc_generator = material_sphinx.DocumentationGenerator(PAGES)
    doc_generator.generate(dest_dir)


if __name__ == "__main__":
    generate(root_dir / "docs" / "sources")
