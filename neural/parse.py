#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: penghuailiang
# @Date  : 2019-04-27

import argparse


def parse_list(str_value):
    if ',' in str_value:
        str_value = str_value.split(',')
    else:
        str_value = [str_value]
    return str_value


parser = argparse.ArgumentParser(description='face')

# ========================== GENERAL PARAMETERS ========================= #
parser.add_argument(
    '--params_cnt',
    dest='params_cnt',
    type=int,
    default=int(95),
    help='count of engine face params')
parser.add_argument(
    '--db_item_cnt',
    dest='db_item_cnt',
    type=int,
    default=int(1600),
    help='count of database item count generated by engine')
parser.add_argument(
    '--path_to_dataset',
    dest='path_to_dataset',
    default="../export/trainset/",
    help='path for database generated by engine')
parser.add_argument(
    '--path_to_testset',
    dest='path_to_testset',
    default="../export/testset/",
    help='path for testset generated by engine')
parser.add_argument(
    '--path_to_inference',
    dest='path_to_inference',
    default="./output/inference/",
    help='model path for inference')
parser.add_argument(
    '--path_tensor_log',
    dest='path_tensor_log',
    default="./logs/",
    help='model path for inference')
parser.add_argument(
    '--phase',
    dest='phase',
    default='train_imitator',
    help='Specify current phase: train or inference.')
parser.add_argument(
    '--use_gpu',
    dest='use_gpu',
    type=bool,
    default=bool(True),
    help='count of engine face params')
parser.add_argument(
    '--gpuid',
    dest='gpuid',
    type=int,
    default=int(0),
    help='device GPU ID')

# ========================= IMITATOR PARAMETERS ========================= #

parser.add_argument(
    '--total_steps',
    dest='total_steps',
    type=int,
    default=int(3e4),
    help='Total number of steps')
parser.add_argument(
    '--batch_size',
    dest='batch_size',
    type=int,
    default=4,
    help='# images in batch')
parser.add_argument(
    '--prev_freq',
    dest='prev_freq',
    type=int,
    default=100,
    help='generate preview image when training')
parser.add_argument(
    '--save_freq',
    dest='save_freq',
    type=int,
    default=500,
    help='Save model every save_freq steps')
parser.add_argument(
    '--lightcnn',
    dest='lightcnn',
    type=str,
    default="./dat/LightCNN_29Layers_V2_checkpoint.pth.tar",
    help='light cnn pre-train model')
parser.add_argument(
    '--learning_rate',
    dest='learning_rate',
    type=float,
    default=0.1,
    help='learning rate of imitator')

# ========================= EXTRACTOR PARAMETERS ========================= #

parser.add_argument(
    '--total_extractor_steps',
    dest='total_extractor_steps',
    type=int,
    default=int(1e3),
    help='Total number of feature extractor steps')
parser.add_argument(
    '--extractor_learning_rate',
    dest='extractor_learning_rate',
    type=float,
    default=0.05,
    help='learning rate of feature extractor')
parser.add_argument(
    '--extractor_save_freq',
    dest='extractor_save_freq',
    type=int,
    default=1000,
    help='Save model every save_freq steps')
