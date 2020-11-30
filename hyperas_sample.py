import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import Sequence
import hyperas as hy
import time
import csv


# Important functions to extract features

def pack(features, label):
  return tf.stack(list(features.values()), axis=-1), label

def get_dataset(file_path,bat_sz,sel_cols,nums):
  dataset = tf.data.experimental.make_csv_dataset(
      file_path,
      batch_size = bat_sz, # Artificially small to make examples easier to show.
      column_defaults = col_types,
      select_columns = sel_cols,
      label_name=LABEL_COLUMN,
      na_value="?",
      num_epochs=nums,
      ignore_errors=True)
  
  packed_data = dataset.map(pack)
  return packed_data


  # Strategy for multicore application

strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
print('Number of devices: {}'.format(strategy.num_replicas_in_sync))

with strategy.scope():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(100, activation='relu', input_shape=(96,)),
        tf.keras.layers.Dense(75, activation='relu'),
        tf.keras.layers.Dense(50, activation='relu'),
        tf.keras.layers.Dense(25, activation='relu'),
        tf.keras.layers.Dropout(0.2), 
        tf.keras.layers.Dense(16)
    ])

    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

file_1 = '/home/madhu/shubhankar/5-fold_NRaa_nr30_relpos/stars_NRaa_nr30_relpos_sp1.csv'
file_2 = '/home/madhu/shubhankar/5-fold_NRaa_nr30_relpos/stars_NRaa_nr30_relpos_sp2.csv'
file_3 = '/home/madhu/shubhankar/5-fold_NRaa_nr30_relpos/stars_NRaa_nr30_relpos_sp3.csv'
file_4 = '/home/madhu/shubhankar/5-fold_NRaa_nr30_relpos/stars_NRaa_nr30_relpos_sp4.csv'
file_5 = '/home/madhu/shubhankar/5-fold_NRaa_nr30_relpos/stars_NRaa_nr30_relpos_sp5.csv'

sel_cols = list(range(1,98))
col_types = ['float32' for i in sel_cols]
LABEL_COLUMN = 'Central Group'
batch_size = 1000
num_epochs = None


start_time = time.time()

file_train = [file_2,file_3,file_4,file_5]

train_data = get_dataset(file_train, batch_size, sel_cols, num_epochs)

ckpt_path_1 = "/home/madhu/shubhankar/5-fold_NRaa_nr30_relpos/train_1/ckpts-{epoch:04d}.ckpt"
ckpt_dir_1 = "/home/madhu/shubhankar/5-fold_NRaa_nr30_relpos/train_1"

cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=ckpt_path_1, 
    verbose=1, 
    save_weights_only=True,
    period=5)

model.save(ckpt_path_1.format(epoch=0))

model.fit(train_data, steps_per_epoch = 36715, epochs = 20, callbacks=[cp_callback])

print("--- %s seconds ---" % (time.time() - start_time))
