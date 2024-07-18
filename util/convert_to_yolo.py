from pylabel import importer

dataset = importer.ImportVOC(path="lcv-annotations")

dataset.export.ExportToYoloV5()