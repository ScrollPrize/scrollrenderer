# Vesuvius Challenge Team 2024
# integrated from ThaumatoAnakalyptor

from setuptools import setup, find_packages

setup(
    name='scroll_renderer',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'tqdm',
        'Pillow',
        'opencv-python',
        'scipy',
        'tifffile',
        'dask',
        'dask-image',
        'zarr',
        'einops',
        'torch',
        'pytorch-lightning',
        'open3d',
        'libigl',
    ],
    entry_points={
        'console_scripts': [
            'slim_uv = scroll_renderer.slim_uv:main',
            'mesh_to_surface = scroll_renderer.mesh_to_surface:main',
            'large_mesh_to_surface = scroll_renderer.large_mesh_to_surface:main',
            'finalize_mesh = scroll_renderer.finalize_mesh:main',
        ],
    },
    author='Vesuvius Challenge Team',
    author_email='team@scrollprize.org',
    description='A package for flattening and rendering 3D meshes of segments of the Herculaneum Papyri.',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
