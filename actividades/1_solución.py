from torch import nn

class Autoencoder(nn.Module):
    
    def __init__(self, n_input=28*28, n_hidden=128, n_latent=2):
        super(type(self), self).__init__()
        
        self.encoder_hidden = nn.ModuleList([nn.Linear(n_input, n_hidden),
                                             nn.ReLU(),
                                             nn.Linear(n_hidden, n_hidden),
                                             nn.ReLU(),
                                             nn.Linear(n_hidden, n_latent)
                                            ])
        
        self.decoder_hidden = nn.ModuleList([nn.Linear(n_latent, n_hidden),
                                             nn.ReLU(),
                                             nn.Linear(n_hidden, n_hidden),
                                             nn.ReLU(),
                                             nn.Linear(n_hidden, n_input)
                                            ])
    
    def encode(self, x):
        for layer in self.encoder_hidden:
            x = layer(x)
        return x
        
    def decode(self, z):
        for layer in self.decoder_hidden:
            z = layer(z)
        return z
    
    def forward(self, x):
        z = self.encode(x)
        return self.decode(z)