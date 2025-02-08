class MusicComposition:
    def __init__(self, name: str, author: str, year: int, duration: int):
        self.name: str = name
        self.author: str = author
        self.year: int = year
        self.duration: int = duration
    
    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Автор: {self.author}\n"
            f"Год выпуска: {self.year}\n"
            f"Продолжительность: {self.duration}"
        )
    def __repr__(self) -> str:
        return f"MusicComposition(name='{self.name}', author='{self.author}', year={self.year}, duration={self.duration})"

class PlayList:
    def __init__(self, name) -> None:
        self.name = name
        self.tracks: list[MusicComposition] = []

    def __iadd__(self, other: MusicComposition) -> 'PlayList':
        if not isinstance(other, MusicComposition):
            raise TypeError("Only MusicComposition objects can be added to a playlist")
        self.tracks.append(other)
        return self

    def __len__(self) -> int:
        return len(self.tracks)

    def __str__(self) -> str:
        return f"{self.name} ({len(self.tracks)} tracks)"
    
    def __add__(self, other: 'PlayList') -> 'PlayList':
        if not isinstance(other, PlayList):
            raise TypeError("Only PlayList objects can be added to a playlist")
        return self.__iadd__(other)
        


composition1 = MusicComposition(
    name="Nothing Else Matters",
    author="James Hetfield, Lars Ulrich",
    year=1991,
    duration=390
)

composition2 = MusicComposition(
    name="Nothing Else Matters",
    author="James Hetfield, Lars Ulrich",
    year=1991,
    duration=390
)

playlist = PlayList(
    name="Metallica"
)
#playlist + composition1
playlist += composition1
playlist += composition2
print(playlist)

        