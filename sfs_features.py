def get_lr_features():
    return [
        'new_window', 'num_window', 'roll_belt', 'pitch_belt', 'yaw_belt', 
        'total_accel_belt', 'kurtosis_roll_belt', 'kurtosis_picth_belt', 
        'kurtosis_yaw_belt', 'skewness_roll_belt', 'skewness_roll_belt.1', 
        'skewness_yaw_belt', 'max_roll_belt', 'max_picth_belt', 
        'max_yaw_belt', 'min_roll_belt', 'min_pitch_belt', 'min_yaw_belt', 
        'amplitude_roll_belt', 'amplitude_pitch_belt', 'amplitude_yaw_belt',
            'var_total_accel_belt', 'avg_roll_belt', 'stddev_roll_belt', 
            'var_roll_belt', 'avg_pitch_belt', 'stddev_pitch_belt', 'var_pitch_belt', 
            'avg_yaw_belt', 'stddev_yaw_belt', 'var_yaw_belt', 'gyros_belt_x', 
            'gyros_belt_y', 'gyros_belt_z', 'accel_belt_x', 'accel_belt_y', 
            'accel_belt_z', 'magnet_belt_x', 'magnet_belt_y', 'magnet_belt_z', 
            'roll_arm', 'pitch_arm', 'yaw_arm', 'total_accel_arm', 'var_accel_arm', 
            'avg_roll_arm', 'stddev_roll_arm', 'var_roll_arm', 'avg_pitch_arm', 
            'stddev_pitch_arm', 'var_pitch_arm', 'avg_yaw_arm', 'stddev_yaw_arm', 
            'var_yaw_arm', 'gyros_arm_x', 'gyros_arm_y', 'gyros_arm_z', 'accel_arm_x', 
            'accel_arm_y', 'accel_arm_z', 'magnet_arm_x', 'kurtosis_roll_arm', 
            'kurtosis_picth_arm', 'kurtosis_yaw_arm', 'skewness_roll_arm', 'skewness_pitch_arm', 
            'skewness_yaw_arm', 'max_roll_arm', 'max_picth_arm', 'max_yaw_arm', 'min_roll_arm', 
            'min_pitch_arm', 'min_yaw_arm', 'amplitude_roll_arm', 'amplitude_pitch_arm', 
            'amplitude_yaw_arm', 'pitch_dumbbell', 'yaw_dumbbell', 'kurtosis_roll_dumbbell', 
            'kurtosis_picth_dumbbell', 'kurtosis_yaw_dumbbell', 'skewness_roll_dumbbell', 
            'skewness_pitch_dumbbell', 'skewness_yaw_dumbbell', 'max_roll_dumbbell', 
            'max_picth_dumbbell', 'max_yaw_dumbbell', 'min_roll_dumbbell', 
            'min_pitch_dumbbell', 'min_yaw_dumbbell', 'amplitude_roll_dumbbell', 
            'amplitude_pitch_dumbbell', 'amplitude_yaw_dumbbell', 'total_accel_dumbbell', 
            'var_accel_dumbbell', 'gyros_dumbbell_y', 'pitch_forearm', 'max_picth_forearm', 
            'max_yaw_forearm', 'min_roll_forearm', 'min_pitch_forearm', 'min_yaw_forearm', 
            'amplitude_roll_forearm', 'amplitude_pitch_forearm', 'amplitude_yaw_forearm', 
            'total_accel_forearm', 'var_accel_forearm', 'avg_roll_forearm', 'stddev_roll_forearm', 
            'var_roll_forearm', 'avg_pitch_forearm', 'stddev_pitch_forearm', 'var_pitch_forearm', 
            'avg_yaw_forearm', 'stddev_yaw_forearm', 'var_yaw_forearm', 'gyros_forearm_x', 
            'gyros_forearm_y', 'gyros_forearm_z', 'accel_forearm_x', 'accel_forearm_y', 
            'accel_forearm_z', 'magnet_forearm_x', 'magnet_forearm_y', 'magnet_forearm_z'
    ]


def get_svm_features():
    return [
        'raw_timestamp_part_1', 'raw_timestamp_part_2', 'new_window', 'num_window', 'pitch_belt', 'yaw_belt', 
        'total_accel_belt', 'kurtosis_roll_belt', 'kurtosis_picth_belt', 'kurtosis_yaw_belt', 'skewness_roll_belt', 
        'skewness_roll_belt.1', 'skewness_yaw_belt', 'max_yaw_belt', 'min_yaw_belt', 'amplitude_roll_belt',
        'amplitude_pitch_belt', 'amplitude_yaw_belt', 'var_total_accel_belt', 'stddev_roll_belt', 'var_roll_belt', 
        'stddev_pitch_belt', 'var_pitch_belt', 'avg_yaw_belt', 'stddev_yaw_belt', 'gyros_belt_x', 'gyros_belt_y', 
        'gyros_belt_z', 'accel_belt_y', 'accel_belt_z', 'magnet_belt_y', 'magnet_belt_z', 'roll_arm', 'total_accel_arm', 
        'stddev_roll_arm', 'avg_pitch_arm', 'var_pitch_arm', 'avg_yaw_arm', 'gyros_arm_x', 'gyros_arm_y', 'gyros_arm_z', 
        'accel_arm_x', 'magnet_arm_z', 'kurtosis_roll_arm', 'kurtosis_picth_arm', 'kurtosis_yaw_arm', 'skewness_roll_arm', 
        'skewness_pitch_arm', 'skewness_yaw_arm', 'max_roll_arm', 'max_picth_arm', 'max_yaw_arm', 'min_pitch_arm', 
        'amplitude_roll_arm', 'kurtosis_roll_dumbbell', 'kurtosis_picth_dumbbell', 'kurtosis_yaw_dumbbell', 
        'skewness_roll_dumbbell', 'skewness_pitch_dumbbell', 'skewness_yaw_dumbbell', 'max_picth_dumbbell', 
        'max_yaw_dumbbell', 'min_yaw_dumbbell', 'amplitude_yaw_dumbbell', 'total_accel_dumbbell', 'var_accel_dumbbell', 
        'avg_roll_dumbbell', 'var_roll_dumbbell', 'avg_pitch_dumbbell', 'stddev_pitch_dumbbell', 'var_pitch_dumbbell', 
        'avg_yaw_dumbbell', 'var_yaw_dumbbell', 'gyros_dumbbell_x', 'gyros_dumbbell_y', 'gyros_dumbbell_z', 
        'magnet_dumbbell_x', 'kurtosis_roll_forearm', 'kurtosis_picth_forearm', 'kurtosis_yaw_forearm', 
        'skewness_roll_forearm', 'skewness_pitch_forearm', 'skewness_yaw_forearm', 'max_roll_forearm', 'max_yaw_forearm', 
        'min_roll_forearm', 'min_pitch_forearm', 'min_yaw_forearm', 'amplitude_roll_forearm', 'amplitude_pitch_forearm', 
        'amplitude_yaw_forearm', 'total_accel_forearm', 'var_accel_forearm', 'avg_roll_forearm', 'stddev_roll_forearm', 
        'var_roll_forearm', 'stddev_pitch_forearm', 'stddev_yaw_forearm', 'gyros_forearm_x', 'gyros_forearm_y', 
        'gyros_forearm_z', 'accel_forearm_x', 'magnet_forearm_z']        


def get_mpl_features():
    return [
        'num_window', 'skewness_roll_belt', 'avg_roll_belt', 'gyros_belt_y', 'roll_arm', 'stddev_roll_arm', 
        'avg_yaw_arm', 'stddev_yaw_arm', 'gyros_arm_x', 'skewness_pitch_arm', 'min_yaw_dumbbell', 
        'kurtosis_picth_forearm', 'max_yaw_forearm', 'avg_pitch_forearm']        