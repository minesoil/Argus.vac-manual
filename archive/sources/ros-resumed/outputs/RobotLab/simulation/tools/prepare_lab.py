"""Check simulator assets before startup without rewriting saved source."""
import math
from workspace_paths import workspace


def circle(radius, count=32):
    """Circumscribed legacy body footprint in base_link coordinates."""
    outer = radius / math.cos(math.pi / count)
    return [[round(-.03 + outer * math.cos(2 * math.pi * i/count), 6),
             round(outer * math.sin(2 * math.pi * i/count), 6)] for i in range(count)]


def prepare():
    package = workspace() / 'src/vacuum_sim'
    for relative in ('launch/sim.launch.py', 'worlds/room.sdf', 'config/controllers.yaml', 'config/drive.rviz'):
        if not (package / relative).is_file():
            raise RuntimeError(f'Missing simulator asset: {relative}. Run tools/install-simulation.py.')


if __name__ == '__main__':
    prepare()
