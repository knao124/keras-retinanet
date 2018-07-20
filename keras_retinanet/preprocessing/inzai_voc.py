from ..preprocessing.pascal_voc import PascalVocGenerator

import os

inzai_classes = {
    '1_単一食材' : 0,
    '2_複数食材' : 1,
    '3_既成品' : 2,
}


class InzaiVocGenerator(PascalVocGenerator):

    def __init__(
        self,
        data_dir,
        set_name,
        classes=inzai_classes,
        image_extension='.jpg',
        skip_truncated=False,
        skip_difficult=False,
        **kwargs
    ):
        self.data_dir             = data_dir
        self.set_name             = set_name
        self.classes              = classes
        self.image_names          = [l.strip() for l in open(os.path.join(data_dir, 'ImageSets', 'Main', set_name + '.txt')).readlines()]
        self.image_extension      = image_extension
        self.skip_truncated       = skip_truncated
        self.skip_difficult       = skip_difficult

        self.labels = {}
        for key, value in self.classes.items():
            self.labels[value] = key

        super(InzaiVocGenerator, self).__init__(data_dir, set_name, **kwargs)
