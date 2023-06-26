from tempfile import TemporaryDirectory, tempdir
import os


# with TemporaryDirectory() as f:
f = tempdir
p = os.path.join(f, "")
assert os.path.exists(p), p