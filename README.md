# engine-sample-assets

The bare minimum of assets that you need to try [piured-engine](https://github.com/piured/engine-native) without running the piured webapp. It has the four default noteskins, the four stages and one song.

## With Docker

Run

```
docker run --rm -p 3333:80 ghcr.io/piured/engine-sample-assets
```

and leave it running. The assets are now served at `http://localhost:3333`, which is where the engine looks for them by default. Open `SongTestScene` in Unity and press play.

## Without Docker

The repo of the engine has a script that does the same with Python. Go to the folder where you cloned the engine and run

```
python3 tools/sample_assets.py
```

The first time it downloads the assets from this repo, and then it serves them at `http://localhost:3333`.

You can also do it by hand. Download `sample-assets.zip` from the [latest release](https://github.com/piured/engine-sample-assets/releases/latest), unpack it and serve the folder that contains `songs`, `noteskins` and `stages` with any web server.

## What is inside

| Folder | Content |
| --- | --- |
| `songs/PIU XX/8 6` | The chart (`song.json`) and the music (`music.mp3`) of one song |
| `noteskins` | `PHOENIX`, `P1`, `P2` and `P3`, which are the noteskins that the engine loads when it starts |
| `stages` | `phoenix`, `xx`, `prime 2` and `zero` |

The format of every file is explained in the [assets documentation](https://github.com/piured/engine-native/blob/main/docs/assets.md) of the engine.

If you want more assets, mail me at pedro.g.bascoy@gmail.com.

## Notice

These files are not ours. The song, the noteskins and the stages belong to their owners, and Pump It Up is a trademark of Andamiro Co., Ltd. We share them here only so that the engine can be tested, with no commercial purpose. If you own any of them and you want it removed, mail me at pedro.g.bascoy@gmail.com and I will remove it.
