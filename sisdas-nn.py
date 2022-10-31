#!/usr/bin/python3
import pandas as pd
import numpy as np
import sys
import math
import random
from pprint import pprint
import matplotlib.pyplot as plt

# Neural Network Stuff

# Creating layer
def create_layer(inp, out):
	layer = []
	# layer tersusun dari perceptron 
	for i in range(0, out):
		# Inialisasi weight awal
		weight = [random.uniform(-0.5, 0.5) for _ in range(inp)]
		# Convert dari List menjadi numpy array
		weight = np.array(weight)
		# Inisialisasi perceptron
		perceptron = {
				"weight": weight,
				"out" : 0,
				"delta":0,
				"in":0,
				"bias":1
				}
		#  tambahkan perceptron menjadi layer
		layer.append(perceptron)
	return layer

def create_network():
	network = []
	# layer input -> hidden layer
	network.append(create_layer(N, M))
	# hidden layer -> layer output
	network.append(create_layer(M, L))
	return network

def feed_forward(x):
	x_in = x
	for layer in network:
		x_out = []
		for perceptron in layer:
			# hasil = v0m + sigma (w * x) 
			hasil = x_in.dot(perceptron["weight"]) + perceptron["bias"]
			# in = zinm
			perceptron["in"] = hasil
			# out = zm = f(zm) 
			perceptron["out"] = sigmoid(hasil)
			x_out.append(perceptron["out"])
		# Maju ke layer selanjutnya
		x_in = np.array(x_out)
	return x_in

def back_propagation(y_decoded):
	one_test_error = 0
	# Loop dari layer paling belakang
	for i in range(len(network)-1, -1, -1):
		# layer output
		layer = network[i]
		for idx, perceptron in (enumerate(layer)):					
			# Jika layer output
			if(len(network)-1 == i):
				# Error diambil dari pengurangan kelas dengan output
				error =  y_decoded[idx] - perceptron["out"]
				# delta diambil untuk update weight
				perceptron["delta"] = error * sigmoid_derivative(perceptron["in"])
				# error kuadrat diambil untuk menghitung msse
				one_test_error += error ** 2
			else:
				# Jika berada di layer sebelumnya (hidden layer)
				# delta in m
				error = 0
				# ambil weight pada layer kanan untuk di propagate
				for perceptron_up in network[i+1]: 
					# delta in m = sigma l (delta l * w(ml))
					error += perceptron_up["weight"][idx] * perceptron["delta"]
				# hitung delta dengan kali delta in m * sigmoid derivative
				perceptron["delta"] = error * sigmoid_derivative(perceptron["in"])
	return one_test_error

def update(x_row):
	for i in range(len(network)):
		layer = network[i]
		# input tidak akan diupdate
		if(i == 0):
			# Input dilayar awal == input data
			inp = x_row
		else:
			# Update perceptron weight
			inp = []
			# ambil layer sebelumnya
			layer_down = network[i-1]
			for i in (layer_down):
				# ambil output nya
				inp.append(i["out"])

		for perceptron in layer:
			for idx in range(len(inp)):
				# update weight
				perceptron['weight'][idx] +=  perceptron['delta'] * inp[idx] * learning_rate 
			# update bias
			perceptron["bias"] +=  perceptron["delta"] * learning_rate 

# Fungsi train_one_row akan melakukan training pada satu row data. 
def train_one_row(x_row, y_row):
	# Urutan algoritma
	# Feer forward -> back_prop -> update
	feed_forward(x_row)
	y_encoded =	encode_y(y_row)
	error_kuadrat = back_propagation(y_encoded)
	update(x_row)
	return error_kuadrat

# Fungsi train_all akan melakukan satu kali epoch (melakukan train terhadap seluruh data train)
def train_all(index_train):
	total_error = 0
	for i in range(len(index_train)):
		idx = index_train[i]
		total_error += train_one_row(atribut[idx], kelas[idx])
	sum_square_error = total_error
	return sum_square_error

# some non nn stuff
def sigmoid(x):
	return 1.0/(1.0+math.exp(-x))

def sigmoid_derivative(x):
	sigm = sigmoid(x)
	return sigm*(1.0-sigm)

def get_max_min(arr):
	for index, row in arr.iterrows():
		if(minimum == -1 or maksimum == 1):
			minimum = row[idx]
			maksimum = row[idx] 
		if (row[idx] < minimum):
			minimum = row[idx]			
		if (row[idx] > maksimum):

			maksimum = row[idx]	
	return (minimum, maksimum)

# normalization to -1 1
def normalization(arr):
	print("[*] Normalize data")
	for idx in range(4):
		mean = arr[idx].mean()
		std = arr[idx].std()
		for index, row in arr.iterrows():
			# z-score
			normalized = (row[idx] - mean)/std 
			arr[idx][index] = normalized
	
	for idx in range(4):
		(minimum, maksimum) = (arr[idx].min(), arr[idx].max())
		for index, row in arr.iterrows():
			# min max 0 1
			normalized = ((row[idx] - minimum)/(maksimum - minimum)) 
			arr[idx][index] = normalized
	

	
			
	print(arr)

# encode y data
# 0 => [1, 0, 0]
# 1 => [0, 1, 0]
# 2 => [0, 0, 1]
def encode_y(idx):
	y_decoded = np.zeros(L)
	y_decoded[idx] = 1
	return y_decoded

# Training perceptron
def full_training():
	# sigma data sigma perceptron x
	global MSSE
	global epoch
	global accuracy_series
	global epoch_series
	global MSSE_series
	epoch = 0
	while((MSSE > 20 or MSSE == 0) and epoch < max_epoch):
		MSSE = train_all(index_train)
		accuracy = test_datatest(index_test)
		print(epoch, accuracy, MSSE)
		accuracy_series.append(accuracy)
		epoch_series.append(epoch)
		MSSE_series.append(MSSE)
		epoch += 1
	return (MSSE, epoch)

# Melakukan feed forward pada input
# Kembaliannya adalah output network
# [y1 y2 y3]
def predict(x_test):
	hasil = feed_forward(x_test)
	return hasil

###########
# seeding agar random tetap saat diulang
def seeding(seed=0):
	random.seed(seed)
	np.random.seed(seed)

# membaca dataset
def read_data(normalized=1, save_normalization=1):
	if(normalized == 1):
		# untuk mempercepat load agar tidak melakukan normalisasi berulang kali
		dataset = pd.read_csv("data_after_normalized.csv", header=None)
	else:	
		# Baca data.csv
		"""
		5.1,3.5,1.4,0.2,Iris-setosa
		4.9,3.0,1.4,0.2,Iris-setosa
		4.7,3.2,1.3,0.2,Iris-setosa
		4.6,3.1,1.5,0.2,Iris-setosa
		5.0,3.6,1.4,0.2,Iris-setosa
		.
		.
		.
		6.7,3.3,5.7,2.5,Iris-virginica
		6.7,3.0,5.2,2.3,Iris-virginica
		6.3,2.5,5.0,1.9,Iris-virginica
		6.5,3.0,5.2,2.0,Iris-virginica
		6.2,3.4,5.4,2.3,Iris-virginica
		5.9,3.0,5.1,1.8,Iris-virginica
		"""
		dataset = pd.read_csv("data.csv", header=None)
		# Merubah kategorik
		dataset.loc[dataset[4]=='Iris-setosa', 4]=0
		dataset.loc[dataset[4]=='Iris-versicolor', 4]=1
		dataset.loc[dataset[4]=='Iris-virginica', 4]=2
		normalization(dataset)
		if(save_normalization == 1):
			dataset.to_csv("data_after_normalized.csv", header=None, index=False)		
	return dataset

# validasi kelas asli dengan prediksi
def validation(kelas_asli, prediksi_encode, method = 0):
	# Validasi menggunakan metode mencari output yang terbesar diantara ketiga output
	# Jika output [0.1 0.3 0.6]
	# Maka hasil prediksi adalah 2
	# Sort dari 0, 1, 2
	benar = True
	# print(kelas_asli)
	# print(prediksi_encode)
	if(method == 0):
		maks = 0
		maks_idx = 0
		# Cari maksimal output dan index nya
		for idx, pred in enumerate(prediksi_encode):		
			if(pred > maks):
				maks_idx = idx
				maks = pred
		# Cek maksimal output dengan kelas sebenarnya
		if(kelas_asli[0] != maks_idx):
			benar = False
	# Validasi menggunakan threshold
	elif(method == 1):
		lower_bond = 0.2
		higher_bond = 0.8
		for i in range(0, 3):
			# thresholding data
			# Jika diatas threshold menjadi 1
			if(prediksi_encode[i] >= higher_bond):
				prediksi_encode[i] = 1
			# Jika dibawah threshol menjadi 0
			elif(prediksi_encode[i] < lower_bond):
				prediksi_encode[i] = 0
			# Jika diantaranya undefine 
			else:
				prediksi_encode[i] = -9999 # undefine
		if(not np.array_equal(encode_y(kelas_asli), prediksi_encode)):
			benar = False
		print(kelas_asli, prediksi_encode)
	return benar

# test_datatest akan melakukan testing pada atribut dan kelas pada index argumen
def test_datatest(index_test):
	jumlah_benar = 0
	# Loop seluruh data
	for i in index_test:
		# Feed forward atribut untuk mendapatkan prediksi
		prediksi = predict(atribut[i])
		# validasi data
		if(validation(kelas[i], prediksi)):
			jumlah_benar += 1
	# return akurasi
	return(jumlah_benar/len(index_test))


# Print hasil klasifikasi
def result():
	print("Hasil klasifikasi pada data IRIS menggunakan Neural Network")
	print("[+] Dimensi Input : {}".format(M))
	print("[+] Hidden Layer : {}".format(N))
	print("[+] Dimensi Output : {}".format(L))
	print("[+] Jumlah Epoch : {}".format(epoch))
	print("[+] Jumlah Data : {}".format(len(dataset)))
	print("[+] Learning Rate : {}".format(learning_rate))
	print("[+] Data Train : {}".format(len(index_train)))
	print("[+] Data Test : {}".format(len(index_test)))
	print("[+] MSSE : {}".format(MSSE))
	print("[+] Akurasi : {}".format(accuracy))
	plt.plot(epoch_series, accuracy_series)
	plt.xlabel('Epoch')
	plt.ylabel('Accuracy')
	plt.title('Diagram epoch terhadap akurasi')
	plt.show()
	plt.plot(epoch_series, MSSE_series)
	plt.xlabel('Epoch')
	plt.ylabel('MSSE')
	plt.title('Diagram epoch terhadap MSSE')
	plt.show()


# Lakukan seeding agar random tetap pada setiap running
seeding()
# Dimensi input
N = 4
# Hidden Layer
M = 10
# Dimensi Output
L = 3
# learning rate
learning_rate = 0.1
print("[*] Read data")
dataset = read_data()
# pisahkan atribut dan kelas
atribut = dataset[[0,1,2,3]].values
kelas = dataset[[4]].values
# initialize network
print("[*] Create network")
# buat network
network = create_network()
# pisahkan index data untuk data train dan data test
perm = np.random.permutation(150)
# index of data train
index_train = perm[0:75]
# index of data test
index_test = perm[75:150]
# max epoch
max_epoch = 1000
# initialize MSSE
MSSE = 0
# epoch
epoch = 0
# train network
accuracy_series = []
MSSE_series = []
epoch_series = []

(MSSE, epoch) = full_training()
print("[*] Train network")
print("[*] Testing data")
print("[*] Get accuracy")

accuracy = test_datatest(index_test)
result()
