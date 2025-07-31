from pathlib import Path



class PathManager:

    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent.parent

    def create_dir(self, *args):
        new_dir = self.base_dir.joinpath(*args)
        if not new_dir.exists():
            new_dir.mkdir(parents=True)
            return new_dir
        # raise FileExistsError(f"Path exists: {new_dir}")
        return new_dir

    def extract_path(self, full_path: Path) -> Path:
        try:
            path_oject = Path(full_path)
            result = path_oject.relative_to(self.base_dir)
            return result
        except ValueError:
            return full_path

    def create_file(self, *args):
        new_file = self.base_dir.joinpath(*args)
        if new_file.exists():
            if new_file.is_file():
                return new_file
            else:
                raise Exception(f"{new_file} is not a file")

        new_file.touch()
        return new_file

    def normalize_extension(self, ext: str) -> str:
        ext = ext.strip().lower()

        if not ext:
            return "."
        return ext if ext[0] == "." else f".{ext}"


# ter = PathManager()
# # print(ter.extract_path(ter.create_dir("logs")))
# print(ter.create_file(ter.extract_path(ter.create_dir("logs")), "test.log"))
#print(ter.extract_path(ter.create_dir("screenshots", "products_page")))
# print(ter.base_dir)

# print(ter.create_dir('screenshots', 'product_page'))

# print(ter.create_file('screenshots/product_page/screen.png'))
