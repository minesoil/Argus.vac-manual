from glob import glob
from setuptools import setup

setup(
    name="argus_avoidance",
    version="0.1.0",
    packages=["argus_avoidance"],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/argus_avoidance"]),
        ("share/argus_avoidance", ["package.xml"]),
        ("share/argus_avoidance/launch", glob("launch/*.launch.py")),
        ("share/argus_avoidance/config", glob("config/*.yaml")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Argus Vac project",
    maintainer_email="argus@example.invalid",
    description="Reactive lidar obstacle avoidance with disabled output defaults",
    license="MIT",
    entry_points={"console_scripts": ["avoidance_controller = argus_avoidance.node:main"]},
)
