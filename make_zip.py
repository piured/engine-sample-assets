"""Builds sample-assets.zip from a folder that has all the assets (songs, noteskins and stages).
Only the files that the engine asks for are copied.

Usage: python3 make_zip.py <folder with the assets>
"""
import os, sys, zipfile

SONGS = [("PIU XX", "8 6")]
NOTESKINS = ["PHOENIX", "P1", "P2", "P3"]
STAGES = ["phoenix", "xx", "prime 2", "zero"]

ARROWS = ["DownLeft", "UpLeft", "Center", "UpRight", "DownRight"]
NOTESKIN_FILES = (["%s %s.PNG" % (arrow, kind) for arrow in ARROWS for kind in ("TapNote 3x2", "Hold 6x1", "Roll 3x2")]
                  + ["Center Receptor 1x2.PNG", "Tap 5x2.PNG", "StepFX 5x1.PNG"])
STAGE_FILES = (["combo.png", "judgment.png", "numbers-normal.png", "numbers-red.png", "stage.png",
                "lifebar-tip.png", "lifebar-pulse.png"]
               + ["lifebar-%s-%s.png" % (style, part) for style in ("single", "double")
                  for part in ("back", "frame", "front", "full-fx", "empty-fx")])
# the zero stage does not have these
OPTIONAL = {"lifebar-pulse.png", "lifebar-single-empty-fx.png", "lifebar-double-empty-fx.png"}

source = sys.argv[1]
wanted = []
for mix, song in SONGS:
    wanted += [("songs/%s/%s/%s" % (mix, song, name), False) for name in ("song.json", "music.mp3")]
for noteskin in NOTESKINS:
    wanted += [("noteskins/%s/UHD/%s" % (noteskin, name), False) for name in NOTESKIN_FILES]
for stage in STAGES:
    wanted += [("stages/%s/%s" % (stage, name), name in OPTIONAL) for name in STAGE_FILES]

missing = [path for path, optional in wanted if not optional and not os.path.isfile(os.path.join(source, path))]
if missing:
    sys.exit("these files are missing in %s:\n  %s" % (source, "\n  ".join(missing)))

total = 0
with zipfile.ZipFile("sample-assets.zip", "w", zipfile.ZIP_STORED) as z:
    for path, optional in wanted:
        full = os.path.join(source, path)
        if os.path.isfile(full):
            z.write(full, path)
            total += 1
print("sample-assets.zip: %d files, %.1f MB" % (total, os.path.getsize("sample-assets.zip") / 1048576))
