import os
from pathlib import Path
from utils.display import repr1


class Paths:
    """Manages and configures the paths used by WaveRNN, Tacotron, and the data."""
    def __init__(self, data_path, voc_id, tts_id):
        self.base = Path(__file__).parent.parent.expanduser().resolve()

        # Data Paths
        self.data = Path(data_path).expanduser().resolve()
        self.quant = self.data/'quant'
        self.mel = self.data/'mel'
        self.gta = self.data/'gta'

        # WaveRNN/Vocoder Paths
        self.voc_checkpoints = self.base/'checkpoints'/'%s.wavernn' % (repr1(voc_id))
        self.voc_latest_weights = self.voc_checkpoints/'latest_weights.pyt'
        self.voc_latest_optim = self.voc_checkpoints/'latest_optim.pyt'
        self.voc_output = self.base/'model_outputs'/'%s.wavernn' % (repr1(voc_id))
        self.voc_step = self.voc_checkpoints/'step.npy'
        self.voc_log = self.voc_checkpoints/'log.txt'

        # Tactron/TTS Paths
        self.tts_checkpoints = self.base/'checkpoints'/'%s.tacotron' % (repr1(tts_id))
        self.tts_latest_weights = self.tts_checkpoints/'latest_weights.pyt'
        self.tts_latest_optim = self.tts_checkpoints/'latest_optim.pyt'
        self.tts_output = self.base/'model_outputs'/'%s.tacotron' % (repr1(tts_id))
        self.tts_step = self.tts_checkpoints/'step.npy'
        self.tts_log = self.tts_checkpoints/'log.txt'
        self.tts_attention = self.tts_checkpoints/'attention'
        self.tts_mel_plot = self.tts_checkpoints/'mel_plots'

        self.create_paths()

    def create_paths(self):
        os.makedirs(self.data, exist_ok=True)
        os.makedirs(self.quant, exist_ok=True)
        os.makedirs(self.mel, exist_ok=True)
        os.makedirs(self.gta, exist_ok=True)
        os.makedirs(self.voc_checkpoints, exist_ok=True)
        os.makedirs(self.voc_output, exist_ok=True)
        os.makedirs(self.tts_checkpoints, exist_ok=True)
        os.makedirs(self.tts_output, exist_ok=True)
        os.makedirs(self.tts_attention, exist_ok=True)
        os.makedirs(self.tts_mel_plot, exist_ok=True)

    def get_tts_named_weights(self, name):
        """Gets the path for the weights in a named tts checkpoint."""
        return self.tts_checkpoints/'%s_weights.pyt' % (repr1(name))

    def get_tts_named_optim(self, name):
        """Gets the path for the optimizer state in a named tts checkpoint."""
        return self.tts_checkpoints/'%s_optim.pyt' % (repr1(name))

    def get_voc_named_weights(self, name):
        """Gets the path for the weights in a named voc checkpoint."""
        return self.voc_checkpoints/'%s_weights.pyt' % (repr1(name))

    def get_voc_named_optim(self, name):
        """Gets the path for the optimizer state in a named voc checkpoint."""
        return self.voc_checkpoints/'%s_optim.pyt' % (repr1(name))


