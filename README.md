# Scroll Renderer

Scroll Renderer is a Python package developed by the Vesuvius Challenge Team 2024. It provides tools for flattening and rendering 3D meshes of segments of the Herculaneum Papyri. It is currently in alpha version.

## Requirements

- **Python 3.11** (no newer versions are currently supported)
- **CUDA 12+** installed on the machine

It is recommended to run this package in a Conda environment to manage dependencies effectively.

## Installation

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/your-repo/scroll_renderer.git
   cd scroll_renderer
   ```

2. Install the package in editable mode:

   ```bash
   pip install -e .
   ```

## Commands

The package provides command-line utilities for working with mesh files. For more options and details on each command, you can use the `--help` option after any command.

### Example Usage

1. **Flatten a Mesh**

   Use the `slim_uv` command to flatten a mesh with the following options:

   ```bash
   slim_uv --path 20241025062044_intermediate_mesh.obj --ic harmonic --iter 200 --um 7.91
   ```

   - `--path`: Path to the intermediate mesh file (e.g., `.obj` file).
   - `--ic`: Initial condition; options are `harmonic` or `arap`.
   - `--iter`: Number of iterations.
   - `--um`: Scaling factor (e.g., `7.91`).

2. **Render a Flattened Mesh**

   After flattening, use `mesh_to_surface` to generate a surface render of the mesh:

   ```bash
   mesh_to_surface 20241025062044_intermediate_mesh_flatboi.obj /mnt/localdisk/scrolls/Scroll5 --r 32
   ```

   - First argument: Path to the flattened mesh file.
   - Second argument: Scroll volume, can be zarr, tifstack or grid cells.
   - `--r`: Half number of layers in the surface volume besides the center (e.g., `32` will give 65 layers, the middle +- 32).

For additional options and usage information, use `--help` with any command (e.g., `slim_uv --help` or `mesh_to_surface --help`).

## License

MIT License

---

**Developed by**: Vesuvius Challenge Tech Team 2024 (Stephen Parsons, Julian Schilliger, Giorgio Angelotti and Youssef Nader)
