import torch
import xml.dom.minidom
from xml.dom.minidom import parse
import utility
import data
import model
import loss
from option import args
from trainer import SRTrainer

torch.manual_seed(args.seed)
checkpoint = utility.checkpoint(args)

def main():
    #global model
    option_file = parse("./options.xml")
    options = option_file.getElementsByTagName("options")[0]

    if checkpoint.ok:
        loader = data.Data(args)
        _model = model.SRModel(args, checkpoint)
        _loss = loss.Loss(args, checkpoint) if not args.test_only else None
        Trainer = SRTrainer(args, loader, _model, _loss, checkpoint)
        while not Trainer.terminate():
            Trainer.train()
            Trainer.test()

        checkpoint.done()

if __name__ == '__main__':
    main()

