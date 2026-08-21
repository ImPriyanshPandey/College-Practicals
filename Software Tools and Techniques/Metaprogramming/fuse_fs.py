from fusepy import FUSE, Operations

class SimpleFS(Operations):
    def readdir(self, path, fh):
        return ['.', '..', 'file.txt']

    def read(self, path, size, offset, fh):
        return b"Hello from FUSE filesystem\n"

if __name__ == '__main__':
    FUSE(SimpleFS(), 'mnt', foreground=True)
