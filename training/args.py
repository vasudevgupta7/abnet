# __author__ = 'Vasudev Gupta'

from dataclasses import dataclass, replace


@dataclass
class Config:

    tr_tgt_file: str
    tr_src_file: str

    val_tgt_file: str
    val_src_file: str

    tst_tgt_file: str
    tst_src_file: str

    max_length: int = 32
    max_target_length: int = 40
    
    tr_max_samples: int = 100
    val_max_samples: int = 20
    tst_max_samples: int = 20

    batch_size: int = 16
    lr: float = 1e-4

    base_dir: str = "base_dir"
    num_workers: int = 2

    load_finetuned_path: str = None # "model_id"
    save_finetuned_path: str = None # "model_id"

    max_epochs: int = 3
    accumulation_steps: int = 1

    save_epoch_dir: str = None
    save_dir: str = None
    load_dir: str = None

    # all these args will be invalid if you run sweep
    project_name: str = 'parallel-decoder-paper'
    wandb_run_name: str = None

iwslt14_de_en = Config(tr_src_file="data/iwslt14/iwslt14.tokenized.de-en/train.de",
                tr_tgt_file="data/iwslt14/iwslt14.tokenized.de-en/train.en",
                val_src_file="data/iwslt14/iwslt14.tokenized.de-en/valid.de",
                val_tgt_file="data/iwslt14/iwslt14.tokenized.de-en/valid.en",
                tst_src_file="data/iwslt14/iwslt14.tokenized.de-en/test.de",
                tst_tgt_file="data/iwslt14/iwslt14.tokenized.de-en/test.en",
                save_finetuned_path="abnet-iwslt14-de-en",
                wandb_run_name="iwslt14-de-en",
                base_dir="iwslt14-de-en")

wmt16_ro_en = Config(tr_src_file="data/wmt16_ro_en/europarl-v8.ro-en.ro",
                tr_tgt_file="data/wmt16_ro_en/europarl-v8.ro-en.en",
                val_src_file="data/wmt16_ro_en/newsdev2016-roen-src.ro.sgm",
                val_tgt_file="data/wmt16_ro_en/newsdev2016-roen-ref.en.sgm",
                tst_src_file="data/wmt16_ro_en/newstest2016-enro-ref.ro.sgm",
                tst_tgt_file="data/wmt16_ro_en/newstest2016-enro-src.en.sgm",
                save_finetuned_path="abnet-wmt16-ro-en",
                wandb_run_name="wmt16-ro-en",
                base_dir="wmt16-ro-en")
