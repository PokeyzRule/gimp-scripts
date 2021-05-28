#!/usr/bin/env python

from gimpfu import *
from os import path


def build_title(image, drawable, title_type, assets_path):
    pdb.gimp_image_convert_rgb(image)
    if title_type == 0:
        event_ranks = ["t1", "t2", "t3", "t10", "t100", "t1000", "t2500", "t5000", "t10000", "tded"
                       ]
        for rank in event_ranks:
            pdb.gimp_image_undo_group_start(image)
            rank_asset = "{}/event_{}.png".format(assets_path, rank)
            new_layer = pdb.gimp_file_load_layer(image, rank_asset)
            pdb.gimp_image_insert_layer(image, new_layer, None, -1)

            # Flatten and save image
            new_image = pdb.gimp_image_duplicate(image)
            layer = pdb.gimp_image_merge_visible_layers(
                new_image, CLIP_TO_IMAGE)
            filename = path.splitext(pdb.gimp_image_get_filename(image))[0]
            save_file = "{}_{}.png".format(filename, rank)
            pdb.file_png_save(new_image, layer, save_file, "event_{}.png".format(
                rank), False, 9, True, False, False, True, True)
            pdb.gimp_image_delete(new_image)
            pdb.gimp_image_remove_layer(image, new_layer)
            pdb.gimp_image_undo_group_end(image)

    elif title_type == 1:
        score_r1_ranks = ["t1",
                          "t2",
                          "t3",
                          "t10",
                          "t100",
                          "tboat"
                          ]
        for rank in score_r1_ranks:
            pdb.gimp_image_undo_group_start(image)
            rank_asset = "{}/score_{}_r1.png".format(assets_path, rank)
            new_layer = pdb.gimp_file_load_layer(image, rank_asset)
            pdb.gimp_image_insert_layer(image, new_layer, None, -1)

            # Flatten and save image
            new_image = pdb.gimp_image_duplicate(image)
            layer = pdb.gimp_image_merge_visible_layers(
                new_image, CLIP_TO_IMAGE)
            filename = path.splitext(pdb.gimp_image_get_filename(image))[0]
            save_file = "{}_{}.png".format(filename, rank)
            pdb.file_png_save(new_image, layer, save_file, "score_{}_r1.png".format(
                rank), False, 9, True, False, False, True, True)
            pdb.gimp_image_delete(new_image)
            pdb.gimp_image_remove_layer(image, new_layer)
            pdb.gimp_image_undo_group_end(image)

    elif title_type == 2:
        score_r2_ranks = ["t1",
                          "t2",
                          "t3",
                          "t10",
                          "t100",
                          "tboat"
                          ]
        for rank in score_r2_ranks:
            pdb.gimp_image_undo_group_start(image)
            rank_asset = "{}/score_{}_r2.png".format(assets_path, rank)
            new_layer = pdb.gimp_file_load_layer(image, rank_asset)
            pdb.gimp_image_insert_layer(image, new_layer, None, -1)

            # Flatten and save image
            new_image = pdb.gimp_image_duplicate(image)
            layer = pdb.gimp_image_merge_visible_layers(
                new_image, CLIP_TO_IMAGE)
            filename = path.splitext(pdb.gimp_image_get_filename(image))[0]
            save_file = "{}_{}.png".format(filename, rank)
            pdb.file_png_save(new_image, layer, save_file, "score_{}_r2.png".format(
                rank), False, 9, True, False, False, True, True)
            pdb.gimp_image_delete(new_image)
            pdb.gimp_image_remove_layer(image, new_layer)
            pdb.gimp_image_undo_group_end(image)

    elif title_type == 3:
        pdb.gimp_image_undo_group_start(image)
        rank_asset = "{}/try_clear_extra.png".format(assets_path)
        new_layer = pdb.gimp_file_load_layer(image, rank_asset)
        pdb.gimp_image_insert_layer(image, new_layer, None, -1)

        # Flatten and save image
        new_image = pdb.gimp_image_duplicate(image)
        layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
        filename = path.splitext(pdb.gimp_image_get_filename(image))[0]
        save_file = "{}_ex.png".format(filename)
        pdb.file_png_save(new_image, layer, save_file, "ex.png",
                          False, 9, True, False, False, True, True)
        pdb.gimp_image_delete(new_image)
        pdb.gimp_image_remove_layer(image, new_layer)
        pdb.gimp_image_undo_group_end(image)

    return


register(
    "bandori_title",
    "Bandori Title Generator\n\nTakes stitched title assets from Bestdori and stitches them together with base title image.\n\n",
    "Takes stitched title assets from Bestdori and stitches them together with base title image.",
    "PokeyzRule",
    "PokeyzRule",
    "2020",
    "<Image>/Bandori/Generate Titles...",
    "*",
    [(PF_OPTION, "title_type", "Title Type", 0, ("Event", "Score (Round 1)", "Score (Round 2)", "EX Title")),
     (PF_DIRNAME, "assets_path", "Assets Location",
      "C:/Users/Gordon/Downloads/Bandori Titles/combined assets")
     ],
    [],
    build_title)

main()
