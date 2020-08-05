## Universidad Austral de Chile
# INFO343: Minería y Aprendizaje con Datos, 2020
# Unidad 5: Redes Neuronales Arficiales

### Responsable: Pablo Huijse H, phuijse@inf.uach.cl

## Contenidos

## Material de la unidad

- [Lecciones asíncronas](https://www.youtube.com/playlist?list=PLEl00Ye9KoHxhz-TrWpqStP7NUJfg0QD9)
- [Láminas de apoyo, lecciones asíncronas](https://docs.google.com/presentation/d/1IJ2n8X4w8pvzNLmpJB-ms6-GDHWthfsJTFuyUqHfXg8/edit?usp=sharing)


## Requisitos de software

Los trabajos prácticos se realizarán en Lenguaje Python 3 usando la librería [PyTorch](https://pytorch.org/)

Para instalar lo más directo es crear un ambiente de conda. Si planeas usar una GPU NVIDIA usar el comando

	conda install pytorch torchvision ignite cudatoolkit=10.2 -c pytorch
	
En caso de no poseer una GPU usar el comando

	conda install pytorch torchvision ignite cpuonly -c pytorch 
	
Adicionalmente, se necesita el ambiente jupyter y algunas librerías del stack científico de Python (NumPy se instalá junto a pytorch)

	conda install ipython jupyter scikit-learn matplotlib

## Bibliografía de la unidad

1. [Ian Goodfellow and Yoshua Bengio and Aaron Courville, "Deep Learning", MIT Press, 2016](https://www.deeplearningbook.org/)
1. [Aston Zhang and Zachary C. Lipton and Mu Li and Alexander J. Smola, "Dive into Deep Learning", 2020](https://www.d2l.ai/)
