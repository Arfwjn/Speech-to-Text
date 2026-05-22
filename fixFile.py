import nbformat

# Ganti dengan nama file notebook Anda
file_path = "STT_Whisper_ONNX_repaired_v3.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Hapus metadata widgets yang bermasalah
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]
    print("Metadata widgets berhasil dihapus.")

with open(file_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
