from glob import glob
from setuptools import setup

setup(
    name="vacuum_hardware",
    version="0.1.0",
    packages=["vacuum_hardware"],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/vacuum_hardware"]),
        ("share/vacuum_hardware", ["package.xml"]),
        ("share/vacuum_hardware/launch", glob("launch/*.launch.py")),
        ("share/vacuum_hardware/config", glob("config/*.yaml")),
        ("share/vacuum_hardware/urdf", glob("urdf/*.urdf")),
    ],
    install_requires=["setuptools", "pyserial"],
    zip_safe=True,
    maintainer="Robot Lab owner",
    maintainer_email="[REDACTED_EMAIL]",
    description="Orange Pi / Mega differential drive",
    license="MIT",
    entry_points={
        "console_scripts": ["motor_bridge = vacuum_hardware.motor_bridge:main"]
    },
)
