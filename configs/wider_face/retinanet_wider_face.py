_base_ = [
    '../_base_/models/retinanet_r50_fpn.py', '../_base_/datasets/wider_face.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_1x.py'
]
model = dict(bbox_head=dict(num_classes=1))
# optimizer
optimizer = dict(_delete_=True, type='Adam', momentum=0.9, lr=0.0002, weight_decay=5e-4)
log_config = dict(interval=1)
optimizer_config = dict(
    _delete_=True, grad_clip=dict(max_norm=35, norm_type=2)
)
