from setuptools import setup

setup(
        name="w-cli",
        version="0.0.1",
        description="Wallpaper manager for macOS",
        author="Yokohide0317",
        install_requires=[],
        entry_points={
            "console_scripts":[
                "w-cli = wallpaper:main"
            ]
        }
)
