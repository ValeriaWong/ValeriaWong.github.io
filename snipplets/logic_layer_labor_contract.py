from keras.layers import Layer
import keras.backend as K

class LaborContractTerminationLayer(Layer):
    def __init__(self, **kwargs):
        super(LaborContractTerminationLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        # No trainable weights
        super(LaborContractTerminationLayer, self).build(input_shape)

    def call(self, x):
        # x应该是一个表示不同终止劳动合同条件的特征向量，例如：
        # - 与工人达成共识
        # - 工人提前通知天数
        # - 工人试用期
        # - 雇主失败条件（例如，未支付、劳动条件）
        # - 工人条件（例如，不符合条件、违反规定）
        # - 无过失解雇条件
        # - 经济减少条件
        # - 等等。

        consensus_with_worker, worker_advance_notice_days, worker_probation_period, employer_failure_conditions, worker_conditions, dismissal_without_fault_conditions, economic_reduction_conditions = x

        # 通过共识终止
        termination_by_consensus = K.cast(K.equal(consensus_with_worker, 1), 'float32')

        # 工人提前通知终止
        termination_by_worker_notice = K.cast(K.greater_equal(worker_advance_notice_days, 30), 'float32') * K.cast(K.equal(worker_probation_period, 0), 'float32') + \
                                       K.cast(K.greater_equal(worker_advance_notice_days, 3), 'float32') * K.cast(K.equal(worker_probation_period, 1), 'float32')

        # 工人单方面终止
        unilateral_by_worker = K.cast(K.greater(employer_failure_conditions, 0), 'float32')

        # 雇主单方面终止
        unilateral_by_employer = K.cast(K.greater(worker_conditions, 0), 'float32')

        # 无过失解雇
        dismissal_without_fault = K.cast(K.greater(dismissal_without_fault_conditions, 0), 'float32')

        # 经济减少
        economic_reduction = K.cast(K.greater(economic_reduction_conditions, 0), 'float32')

        # 组合所有条件
        termination = termination_by_consensus + termination_by_worker_notice + unilateral_by_worker + unilateral_by_employer + dismissal_without_fault + economic_reduction

        return K.cast(K.greater(termination, 0), 'float32')

    def compute_output_shape(self, input_shape):
        return input_shape[0]

