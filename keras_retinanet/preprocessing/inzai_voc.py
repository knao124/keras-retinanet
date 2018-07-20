from ..preprocessing.pascal_voc import PascalVocGenerator

import os

inzai_classes = {
    '1_単一食材' : 0,
    '2_複数食材' : 1,
    '3_既成品' : 2,
}


class InzaiVocGenerator(PascalVocGenerator):

    def __init__(self, data_dir, set_name, **kwargs):
        super(InzaiVocGenerator, self).__init__(data_dir, set_name, classes=inzai_classes, **kwargs)

        # spaceが入ってるfilenameに対応する
        filepath = os.path.join(data_dir, 'ImageSets', 'Main', set_name + '.txt')
        self.image_names = [l.strip() for l in open(filepath).readlines()]
