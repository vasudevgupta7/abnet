# __author__ = 'Vasudev Gupta'

import torch
from training.torch_trainer import TorchTrainer
from tqdm import tqdm
import os


class Trainer(TorchTrainer):

    def __init__(self, model, tokenizer, args):

        self.model = model
        self.tokenizer = tokenizer
        self.lr = args.lr
        self.args = args

        super().__init__(args)

    def configure_optimizers(self):
        return torch.optim.Adam(self.model.parameters(), lr=self.lr)

    def training_step(self, batch, batch_idx):
        # dynamic masking over decoder_input_ids
        out = self.tokenizer.mask_decoder_ids(batch["decoder_input_ids"])
        batch["decoder_input_ids"] = out.pop("masked_decoder_ids")

        for k in batch:
            batch[k] = batch[k].to(self.device)

        # TODO: complete it whenever loss_fn is ready
        loss_mask = out.pop("mask_ids")

        out = self.model(**batch, return_dict=True)
        loss, length_loss, translation_loss = self.compute_loss(out["logits"], batch["labels"], out["length_logits"], loss_mask, eps=.1, pad_id=0, reduction="sum")
        self.log(length_loss=length_loss, translation_loss=translation_loss)
        return loss

    @torch.no_grad()
    def validation_step(self, batch):
        # dynamic masking over decoder_input_ids
        out = self.tokenizer.mask_decoder_ids(batch["decoder_input_ids"])
        batch["decoder_input_ids"] = out.pop("masked_decoder_ids")

        for k in batch:
            batch[k] = batch[k].to(self.device)

        # TODO: complete it whenever loss_fn is ready
        loss_mask = out.pop("mask_ids")

        out = self.model(**batch, return_dict=True)
        loss, length_loss, translation_loss = self.model.compute_loss(out["logits"], batch["labels"], out["length_logits"], loss_mask, eps=.1, pad_id=0, reduction="sum")
        self.log(length_loss=length_loss, translation_loss=translation_loss)

        return loss

    def training_epoch_end(self, epoch, losses):

        save_pretrained_path = self.args.save_pretrained_path
        if save_pretrained_path:
            self.model.save_pretrained(save_pretrained_path)
        if self.args.save_training_state:
            self.save_training_state_dict(self.args.base_dir)
