# vacuum-workspace-source.tar.gz

Historical source: ros-original


## src

## src/vacuum_sim

## src/vacuum_sim/package.xml

<?xml version="1.0"?>
<package format="3">
  <name>vacuum_sim</name><version>0.1.0</version>
  <description>Starter vacuum robot simulation with explicitly provisional geometry.</description>
  <maintainer email="[REDACTED_EMAIL]">Local robot developer</maintainer>
  <license>Apache-2.0</license>
  <buildtool_depend>ament_cmake</buildtool_depend>
  <exec_depend>ament_index_python</exec_depend><exec_depend>launch</exec_depend><exec_depend>launch_ros</exec_depend>
  <exec_depend>rclpy</exec_depend><exec_depend>geometry_msgs</exec_depend>
  <exec_depend>robot_state_publisher</exec_depend><exec_depend>xacro</exec_depend>
  <exec_depend>ros_gz_sim</exec_depend><exec_depend>ros_gz_bridge</exec_depend>
  <exec_depend>gz_ros2_control</exec_depend><exec_depend>controller_manager</exec_depend>
  <exec_depend>diff_drive_controller</exec_depend><exec_depend>joint_state_broadcaster</exec_depend>
  <exec_depend>rviz2</exec_depend><exec_depend>slam_toolbox</exec_depend>
  <exec_depend>nav2_bringup</exec_depend><exec_depend>python3-yaml</exec_depend>
  <export><build_type>ament_cmake</build_type></export>
</package>


## src/vacuum_sim/config

## src/vacuum_sim/config/view.rviz

Panels:
  - Class: rviz_common/Displays
    Help Height: 70
    Name: Displays
    Property Tree Widget:
      Expanded: ~
      Splitter Ratio: 0.5
    Tree Height: 208
  - Class: rviz_common/Tool Properties
    Expanded: ~
    Name: Tool Properties
    Splitter Ratio: 0.5
Visualization Manager:
  Class: ""
  Displays:
    - Alpha: 0.5
      Cell Size: 0.5
      Class: rviz_default_plugins/Grid
      Color: 160; 160; 164
      Enabled: true
      Line Style:
        Line Width: 0.029999999329447746
        Value: Lines
      Name: Grid
      Normal Cell Count: 0
      Offset:
        X: 0
        Y: 0
        Z: 0
      Plane: XY
      Plane Cell Count: 20
      Reference Frame: <Fixed Frame>
      Value: true
    - Alpha: 1
      Class: rviz_default_plugins/RobotModel
      Collision Enabled: false
      Description File: ""
      Description Source: Topic
      Description Topic:
        Depth: 5
        Durability Policy: Transient Local
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /robot_description
      Enabled: true
      Links:
        All Links Enabled: true
        Expand Joint Details: false
        Expand Link Details: false
        Expand Tree: false
        Link Tree Style: Links in Alphabetic Order
        base_footprint:
          Alpha: 1
          Show Axes: false
          Show Trail: false
        base_link:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        camera_link:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        camera_optical_frame:
          Alpha: 1
          Show Axes: false
          Show Trail: false
        caster:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        left_wheel:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        lidar_link:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        right_wheel:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
      Mass Properties:
        Inertia: false
        Mass: false
      Name: Robot
      TF Prefix: ""
      Update Interval: 0
      Value: true
      Visual Enabled: true
    - Alpha: 1
      Autocompute Intensity Bounds: true
      Autocompute Value Bounds:
        Max Value: 10
        Min Value: -10
        Value: true
      Axis: Z
      Channel Name: intensity
      Class: rviz_default_plugins/LaserScan
      Color: 255; 255; 255
      Color Transformer: Intensity
      Decay Time: 0
      Enabled: true
      Invert Rainbow: false
      Max Color: 255; 255; 255
      Max Intensity: 0
      Min Color: 0; 0; 0
      Min Intensity: 0
      Name: Lidar
      Position Transformer: XYZ
      Selectable: true
      Size (Pixels): 3
      Size (m): 0.02500000037252903
      Style: Flat Squares
      Topic:
        Depth: 5
        Durability Policy: Volatile
        Filter size: 10
        History Policy: Keep Last
        Reliability Policy: Best Effort
        Value: /scan
      Use Fixed Frame: true
      Use rainbow: true
      Value: true
    - Alpha: 0.699999988079071
      Binary representation: false
      Binary threshold: 100
      Class: rviz_default_plugins/Map
      Color Scheme: map
      Draw Behind: false
      Enabled: true
      Name: Map
      Topic:
        Depth: 5
        Durability Policy: Transient Local
        Filter size: 10
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /map
      Update Topic:
        Depth: 5
        Durability Policy: Volatile
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /map_updates
      Use Timestamp: false
      Value: true
    - Class: rviz_default_plugins/Image
      Enabled: true
      Max Value: 1
      Median window: 5
      Min Value: 0
      Name: Camera
      Normalize Range: true
      Topic:
        Depth: 5
        Durability Policy: Volatile
        History Policy: Keep Last
        Reliability Policy: Best Effort
        Value: /camera/image_raw
      Value: true
  Enabled: true
  Global Options:
    Background Color: 35; 40; 48
    Fixed Frame: odom
    Frame Rate: 15
  Name: root
  Tools:
    - Class: rviz_default_plugins/Interact
      Hide Inactive Objects: true
    - Class: rviz_default_plugins/MoveCamera
    - Class: rviz_default_plugins/Select
    - Class: nav2_rviz_plugins/GoalTool
  Transformation:
    Current:
      Class: rviz_default_plugins/TF
  Value: true
  Views:
    Current:
      Class: rviz_default_plugins/Orbit
      Distance: 6
      Enable Stereo Rendering:
        Stereo Eye Separation: 0.05999999865889549
        Stereo Focal Distance: 1
        Swap Stereo Eyes: false
        Value: false
      Focal Point:
        X: 0
        Y: 0
        Z: 0
      Focal Shape Fixed Size: true
      Focal Shape Size: 0.05000000074505806
      Invert Z Axis: false
      Name: Current View
      Near Clip Distance: 0.009999999776482582
      Pitch: 0.800000011920929
      Target Frame: <Fixed Frame>
      Value: Orbit (rviz_default_plugins)
      Yaw: 0.800000011920929
    Saved: ~
Window Geometry:
  Camera:
    collapsed: false
  Displays:
    collapsed: false
  Height: 800
  Hide Left Dock: false
  Hide Right Dock: false
  QMainWindow State: 000000ff00000000fd000000010000000000000156000002cafc0200000003fb0000000c00430061006d006500720061010000003b000000c90000001600fffffffb000000100044006900730070006c006100790073010000010a00000151000000c700fffffffb0000001e0054006f006f006c002000500072006f00700065007200740069006500730100000261000000a40000005c00ffffff00000354000002ca00000004000000040000000800000008fc0000000100000002000000010000000a0054006f006f006c00730100000000ffffffff0000000000000000
  Tool Properties:
    collapsed: false
  Width: 1200
  X: 1934
  Y: 40


## src/vacuum_sim/config/bridge.yaml

- ros_topic_name: /clock
  gz_topic_name: /clock
  ros_type_name: rosgraph_msgs/msg/Clock
  gz_type_name: gz.msgs.Clock
  direction: GZ_TO_ROS
- ros_topic_name: /scan
  gz_topic_name: /scan
  ros_type_name: sensor_msgs/msg/LaserScan
  gz_type_name: gz.msgs.LaserScan
  direction: GZ_TO_ROS
  qos_profile: SENSOR_DATA
- ros_topic_name: /camera/image_raw
  gz_topic_name: /camera/image_raw
  ros_type_name: sensor_msgs/msg/Image
  gz_type_name: gz.msgs.Image
  direction: GZ_TO_ROS
  qos_profile: SENSOR_DATA
- ros_topic_name: /camera/camera_info
  gz_topic_name: /camera/camera_info
  ros_type_name: sensor_msgs/msg/CameraInfo
  gz_type_name: gz.msgs.CameraInfo
  direction: GZ_TO_ROS
  qos_profile: SENSOR_DATA


## src/vacuum_sim/config/nav2.yaml

amcl:
  ros__parameters:
    alpha1: 0.2
    alpha2: 0.2
    alpha3: 0.2
    alpha4: 0.2
    alpha5: 0.2
    base_frame_id: base_footprint
    beam_skip_distance: 0.5
    beam_skip_error_threshold: 0.9
    beam_skip_threshold: 0.3
    do_beamskip: false
    global_frame_id: map
    lambda_short: 0.1
    laser_likelihood_max_dist: 2.0
    laser_max_range: 100.0
    laser_min_range: -1.0
    laser_model_type: likelihood_field
    max_beams: 60
    max_particles: 2000
    min_particles: 500
    odom_frame_id: odom
    pf_err: 0.05
    pf_z: 0.99
    recovery_alpha_fast: 0.0
    recovery_alpha_slow: 0.0
    resample_interval: 1
    robot_model_type: nav2_amcl::DifferentialMotionModel
    save_pose_rate: 0.5
    sigma_hit: 0.2
    tf_broadcast: true
    transform_tolerance: 1.0
    update_min_a: 0.2
    update_min_d: 0.25
    z_hit: 0.5
    z_max: 0.05
    z_rand: 0.5
    z_short: 0.05
    scan_topic: scan
    use_sim_time: true
bt_navigator:
  ros__parameters:
    global_frame: map
    robot_base_frame: base_footprint
    odom_topic: /odom
    bt_loop_duration: 10
    default_server_timeout: 20
    wait_for_service_timeout: 1000
    action_server_result_timeout: 900.0
    navigators:
    - navigate_to_pose
    - navigate_through_poses
    navigate_to_pose:
      plugin: nav2_bt_navigator::NavigateToPoseNavigator
    navigate_through_poses:
      plugin: nav2_bt_navigator::NavigateThroughPosesNavigator
    error_code_names:
    - compute_path_error_code
    - follow_path_error_code
    use_sim_time: true
    enable_stamped_cmd_vel: false
controller_server:
  ros__parameters:
    controller_frequency: 20.0
    costmap_update_timeout: 0.3
    min_x_velocity_threshold: 0.001
    min_y_velocity_threshold: 0.5
    min_theta_velocity_threshold: 0.001
    failure_tolerance: 0.3
    progress_checker_plugins:
    - progress_checker
    goal_checker_plugins:
    - general_goal_checker
    controller_plugins:
    - FollowPath
    use_realtime_priority: false
    progress_checker:
      plugin: nav2_controller::SimpleProgressChecker
      required_movement_radius: 0.15
      movement_time_allowance: 30.0
    general_goal_checker:
      stateful: true
      plugin: nav2_controller::SimpleGoalChecker
      xy_goal_tolerance: 0.15
      yaw_goal_tolerance: 0.25
    FollowPath:
      plugin: dwb_core::DWBLocalPlanner
      debug_trajectory_details: false
      min_vel_x: -0.15
      max_vel_x: 0.25
      min_vel_y: 0.0
      max_vel_y: 0.0
      max_vel_theta: 1.0
      min_speed_xy: 0.0
      max_speed_xy: 0.25
      min_speed_theta: 0.0
      acc_lim_x: 0.3
      acc_lim_y: 0.0
      acc_lim_theta: 1.0
      decel_lim_x: -0.3
      decel_lim_y: 0.0
      decel_lim_theta: -1.0
      vx_samples: 20
      vy_samples: 1
      vtheta_samples: 20
      sim_time: 1.7
      linear_granularity: 0.05
      angular_granularity: 0.025
      transform_tolerance: 0.2
      xy_goal_tolerance: 0.15
      trans_stopped_velocity: 0.02
      short_circuit_trajectory_evaluation: true
      stateful: true
      critics:
      - RotateToGoal
      - Oscillation
      - BaseObstacle
      - GoalAlign
      - PathAlign
      - PathDist
      - GoalDist
      BaseObstacle.scale: 0.02
      PathAlign.scale: 32.0
      PathAlign.forward_point_distance: 0.1
      GoalAlign.scale: 24.0
      GoalAlign.forward_point_distance: 0.1
      PathDist.scale: 32.0
      GoalDist.scale: 24.0
      RotateToGoal.scale: 32.0
      RotateToGoal.slowing_factor: 5.0
      RotateToGoal.lookahead_time: -1.0
    use_sim_time: true
    odom_topic: /odom
    enable_stamped_cmd_vel: false
local_costmap:
  local_costmap:
    ros__parameters:
      update_frequency: 5.0
      publish_frequency: 2.0
      global_frame: odom
      robot_base_frame: base_footprint
      rolling_window: true
      width: 3
      height: 3
      resolution: 0.05
      robot_radius: 0.22
      plugins:
      - voxel_layer
      - inflation_layer
      inflation_layer:
        plugin: nav2_costmap_2d::InflationLayer
        cost_scaling_factor: 3.0
        inflation_radius: 0.35
      voxel_layer:
        plugin: nav2_costmap_2d::VoxelLayer
        enabled: true
        publish_voxel_map: true
        origin_z: 0.0
        z_resolution: 0.05
        z_voxels: 16
        max_obstacle_height: 2.0
        mark_threshold: 0
        observation_sources: scan
        scan:
          topic: /scan
          max_obstacle_height: 2.0
          clearing: true
          marking: true
          data_type: LaserScan
          raytrace_max_range: 8.0
          raytrace_min_range: 0.0
          obstacle_max_range: 6.0
          obstacle_min_range: 0.0
      static_layer:
        plugin: nav2_costmap_2d::StaticLayer
        map_subscribe_transient_local: true
      always_send_full_costmap: true
      use_sim_time: true
global_costmap:
  global_costmap:
    ros__parameters:
      update_frequency: 1.0
      publish_frequency: 1.0
      global_frame: map
      robot_base_frame: base_footprint
      robot_radius: 0.22
      resolution: 0.05
      track_unknown_space: true
      plugins:
      - static_layer
      - obstacle_layer
      - inflation_layer
      obstacle_layer:
        plugin: nav2_costmap_2d::ObstacleLayer
        enabled: true
        observation_sources: scan
        scan:
          topic: /scan
          max_obstacle_height: 2.0
          clearing: true
          marking: true
          data_type: LaserScan
          raytrace_max_range: 8.0
          raytrace_min_range: 0.0
          obstacle_max_range: 6.0
          obstacle_min_range: 0.0
      static_layer:
        plugin: nav2_costmap_2d::StaticLayer
        map_subscribe_transient_local: true
      inflation_layer:
        plugin: nav2_costmap_2d::InflationLayer
        cost_scaling_factor: 3.0
        inflation_radius: 0.35
      always_send_full_costmap: true
      use_sim_time: true
map_saver:
  ros__parameters:
    save_map_timeout: 5.0
    free_thresh_default: 0.25
    occupied_thresh_default: 0.65
    map_subscribe_transient_local: true
    use_sim_time: true
planner_server:
  ros__parameters:
    expected_planner_frequency: 20.0
    planner_plugins:
    - GridBased
    costmap_update_timeout: 1.0
    GridBased:
      plugin: nav2_navfn_planner::NavfnPlanner
      tolerance: 0.5
      use_astar: false
      allow_unknown: false
    use_sim_time: true
smoother_server:
  ros__parameters:
    smoother_plugins:
    - simple_smoother
    simple_smoother:
      plugin: nav2_smoother::SimpleSmoother
      tolerance: 1.0e-10
      max_its: 1000
      do_refinement: true
    use_sim_time: true
behavior_server:
  ros__parameters:
    local_costmap_topic: local_costmap/costmap_raw
    global_costmap_topic: global_costmap/costmap_raw
    local_footprint_topic: local_costmap/published_footprint
    global_footprint_topic: global_costmap/published_footprint
    cycle_frequency: 10.0
    behavior_plugins:
    - spin
    - backup
    - drive_on_heading
    - assisted_teleop
    - wait
    spin:
      plugin: nav2_behaviors::Spin
    backup:
      plugin: nav2_behaviors::BackUp
    drive_on_heading:
      plugin: nav2_behaviors::DriveOnHeading
    wait:
      plugin: nav2_behaviors::Wait
    assisted_teleop:
      plugin: nav2_behaviors::AssistedTeleop
    local_frame: odom
    global_frame: map
    robot_base_frame: base_footprint
    transform_tolerance: 0.1
    simulate_ahead_time: 2.0
    max_rotational_vel: 1.0
    min_rotational_vel: 0.4
    rotational_acc_lim: 3.2
    use_sim_time: true
    odom_topic: /odom
    enable_stamped_cmd_vel: false
waypoint_follower:
  ros__parameters:
    loop_rate: 20
    stop_on_failure: false
    action_server_result_timeout: 900.0
    waypoint_task_executor_plugin: wait_at_waypoint
    wait_at_waypoint:
      plugin: nav2_waypoint_follower::WaitAtWaypoint
      enabled: true
      waypoint_pause_duration: 200
    use_sim_time: true
route_server:
  ros__parameters:
    boundary_radius_to_achieve_node: 1.0
    radius_to_achieve_node: 2.0
    smooth_corners: true
    operations:
    - AdjustSpeedLimit
    - ReroutingService
    - CollisionMonitor
    ReroutingService:
      plugin: nav2_route::ReroutingService
    AdjustSpeedLimit:
      plugin: nav2_route::AdjustSpeedLimit
    CollisionMonitor:
      plugin: nav2_route::CollisionMonitor
      max_collision_dist: 3.0
    edge_cost_functions:
    - DistanceScorer
    - CostmapScorer
    DistanceScorer:
      plugin: nav2_route::DistanceScorer
    CostmapScorer:
      plugin: nav2_route::CostmapScorer
    use_sim_time: true
velocity_smoother:
  ros__parameters:
    smoothing_frequency: 20.0
    stamp_smoothed_velocity_with_smoothing_time: false
    scale_velocities: false
    feedback: OPEN_LOOP
    max_velocity:
    - 0.25
    - 0.0
    - 1.0
    min_velocity:
    - -0.15
    - 0.0
    - -1.0
    max_accel:
    - 0.3
    - 0.0
    - 1.0
    max_decel:
    - -0.3
    - 0.0
    - -1.0
    odom_topic: /odom
    odom_duration: 0.1
    deadband_velocity:
    - 0.0
    - 0.0
    - 0.0
    velocity_timeout: 0.5
    use_sim_time: true
    enable_stamped_cmd_vel: false
collision_monitor:
  ros__parameters:
    base_frame_id: base_footprint
    odom_frame_id: odom
    cmd_vel_in_topic: cmd_vel_smoothed
    cmd_vel_out_topic: cmd_vel
    state_topic: collision_monitor_state
    transform_tolerance: 0.2
    source_timeout: 1.0
    base_shift_correction: true
    stop_pub_timeout: 2.0
    polygons:
    - FootprintApproach
    FootprintApproach:
      type: polygon
      action_type: approach
      footprint_topic: /local_costmap/published_footprint
      time_before_collision: 1.2
      simulation_time_step: 0.1
      min_points: 6
      visualize: false
      enabled: true
    observation_sources:
    - scan
    scan:
      type: scan
      topic: scan
      min_height: 0.15
      max_height: 2.0
      enabled: true
    use_sim_time: true
    enable_stamped_cmd_vel: false
docking_server:
  ros__parameters:
    controller_frequency: 50.0
    initial_perception_timeout: 5.0
    wait_charge_timeout: 5.0
    dock_approach_timeout: 30.0
    undock_linear_tolerance: 0.05
    undock_angular_tolerance: 0.1
    max_retries: 3
    base_frame: base_footprint
    fixed_frame: odom
    dock_backwards: false
    dock_prestaging_tolerance: 0.5
    dock_plugins:
    - simple_charging_dock
    simple_charging_dock:
      plugin: opennav_docking::SimpleChargingDock
      docking_threshold: 0.05
      staging_x_offset: -0.7
      use_external_detection_pose: true
      use_battery_status: false
      use_stall_detection: false
      external_detection_timeout: 1.0
      external_detection_translation_x: -0.18
      external_detection_translation_y: 0.0
      external_detection_rotation_roll: -1.57
      external_detection_rotation_pitch: -1.57
      external_detection_rotation_yaw: 0.0
      filter_coef: 0.1
    controller:
      k_phi: 3.0
      k_delta: 2.0
      v_linear_min: 0.15
      v_linear_max: 0.15
      use_collision_detection: true
      costmap_topic: local_costmap/costmap_raw
      footprint_topic: local_costmap/published_footprint
      transform_tolerance: 0.1
      projection_time: 5.0
      simulation_step: 0.1
      dock_collision_threshold: 0.3
    use_sim_time: true
    enable_stamped_cmd_vel: false
loopback_simulator:
  ros__parameters:
    base_frame_id: base_footprint
    odom_frame_id: odom
    map_frame_id: map
    scan_frame_id: base_scan
    update_duration: 0.02
    scan_range_min: 0.05
    scan_range_max: 30.0
    scan_angle_min: -3.1415
    scan_angle_max: 3.1415
    scan_angle_increment: 0.02617
    scan_use_inf: true
    use_sim_time: true


## src/vacuum_sim/config/slam.yaml

slam_toolbox:
  ros__parameters:
    use_sim_time: true
    mode: mapping
    odom_frame: odom
    map_frame: map
    base_frame: base_footprint
    scan_topic: /scan
    resolution: 0.05
    max_laser_range: 12.0
    minimum_travel_distance: 0.1
    minimum_travel_heading: 0.15
    map_update_interval: 2.0
    transform_publish_period: 0.02
    transform_timeout: 0.2
    tf_buffer_duration: 30.0
    scan_queue_size: 1
    use_scan_matching: true
    use_scan_barycenter: true
    solver_plugin: solver_plugins::CeresSolver
    ceres_linear_solver: SPARSE_NORMAL_CHOLESKY
    ceres_preconditioner: SCHUR_JACOBI
    ceres_trust_strategy: LEVENBERG_MARQUARDT
    ceres_dogleg_type: TRADITIONAL_DOGLEG
    ceres_loss_function: None


## src/vacuum_sim/config/controllers.yaml

controller_manager:
  ros__parameters:
    update_rate: 50
    use_sim_time: true
    joint_state_broadcaster:
      type: joint_state_broadcaster/JointStateBroadcaster
    diff_drive_controller:
      type: diff_drive_controller/DiffDriveController

diff_drive_controller:
  ros__parameters:
    use_sim_time: true
    left_wheel_names: [left_wheel_joint]
    right_wheel_names: [right_wheel_joint]
    wheel_separation: 0.29
    wheel_radius: 0.05
    publish_rate: 30.0
    odom_frame_id: odom
    base_frame_id: base_footprint
    enable_odom_tf: true
    open_loop: false
    position_feedback: true
    cmd_vel_timeout: 0.5
    pose_covariance_diagonal: [0.001, 0.001, 0.001, 0.001, 0.001, 0.01]
    twist_covariance_diagonal: [0.001, 0.001, 0.001, 0.001, 0.001, 0.01]
    linear.x.has_velocity_limits: true
    linear.x.max_velocity: 0.25
    linear.x.min_velocity: -0.15
    linear.x.has_acceleration_limits: true
    linear.x.max_acceleration: 0.3
    linear.x.min_acceleration: -0.3
    angular.z.has_velocity_limits: true
    angular.z.max_velocity: 1.0
    angular.z.min_velocity: -1.0
    angular.z.has_acceleration_limits: true
    angular.z.max_acceleration: 1.0
    angular.z.min_acceleration: -1.0


## src/vacuum_sim/launch

## src/vacuum_sim/launch/mapping.launch.py

from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    slam = Path(get_package_share_directory('slam_toolbox'))
    return LaunchDescription([IncludeLaunchDescription(
        PythonLaunchDescriptionSource(str(slam / 'launch/online_async_launch.py')),
        launch_arguments={'use_sim_time': 'true', 'slam_params_file': str(package / 'config/slam.yaml')}.items())])


## src/vacuum_sim/launch/navigation.launch.py

"""Start navigation against the map published by the separate mapping launch."""
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    config = package / 'config/nav2.yaml'
    if not config.exists():
        raise RuntimeError('Generate config with tools/prepare_nav2.py in Ubuntu and rebuild first.')
    nav2 = Path(get_package_share_directory('nav2_bringup'))
    return LaunchDescription([IncludeLaunchDescription(
        PythonLaunchDescriptionSource(str(nav2 / 'launch/navigation_launch.py')),
        launch_arguments={'use_sim_time': 'true', 'params_file': str(config),
                          'autostart': 'true', 'use_composition': 'False'}.items())])


## src/vacuum_sim/launch/sim.launch.py

from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler, SetEnvironmentVariable, ExecuteProcess
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    gz_launch = str(Path(get_package_share_directory('ros_gz_sim')) / 'launch' / 'gz_sim.launch.py')
    description = ParameterValue(Command(['xacro ', str(package / 'urdf/vacuum.urdf.xacro'), ' camera_width:=', LaunchConfiguration('camera_width'), ' camera_height:=', LaunchConfiguration('camera_height'), ' camera_rate:=', LaunchConfiguration('camera_rate')]), value_type=str)
    spawn = Node(package='ros_gz_sim', executable='create', arguments=[
        '-world', 'vacuum_room', '-name', 'vacuum', '-topic', '/robot_description', '-z', '0.015'], output='screen')
    controllers = Node(package='controller_manager', executable='spawner', arguments=[
        'joint_state_broadcaster', 'diff_drive_controller', '--controller-manager-timeout', '120'], output='screen')
    return LaunchDescription([
        DeclareLaunchArgument('camera_width', default_value='320'),
        DeclareLaunchArgument('camera_height', default_value='240'),
        DeclareLaunchArgument('camera_rate', default_value='5'),
        DeclareLaunchArgument('gui', default_value='true'),
        DeclareLaunchArgument('rviz', default_value='true'),
        SetEnvironmentVariable('ROS_AUTOMATIC_DISCOVERY_RANGE', 'LOCALHOST'),
        SetEnvironmentVariable('ROS_DOMAIN_ID', '42'),
        SetEnvironmentVariable('GZ_PARTITION', 'vacuum_sim_42'),
        SetEnvironmentVariable('GZ_IP', '127.0.0.1'),
        # Direct argv keeps Gazebo under launch's signal handling; a shell wrapper
        # previously exited first and left its Gazebo child running.
        ExecuteProcess(cmd=['gz', 'sim', '-r', '-s', '-v', '2', str(package / 'worlds/room.sdf')], output='screen'),
        ExecuteProcess(cmd=['gz', 'sim', '-g', '-v', '2'], output='screen', condition=IfCondition(LaunchConfiguration('gui'))),
        Node(package='robot_state_publisher', executable='robot_state_publisher',
             parameters=[{'robot_description': description, 'use_sim_time': True}], output='screen'),
        Node(package='ros_gz_bridge', executable='parameter_bridge', parameters=[
            {'config_file': str(package / 'config/bridge.yaml'), 'use_sim_time': True}], output='screen'),
        RegisterEventHandler(OnProcessExit(target_action=spawn, on_exit=[controllers])),
        spawn,
        Node(package='vacuum_sim', executable='twist_adapter.py', parameters=[{'use_sim_time': True}], output='screen'),
        Node(package='rviz2', executable='rviz2', arguments=['-d', str(package / 'config/view.rviz')],
             parameters=[{'use_sim_time': True}], condition=IfCondition(LaunchConfiguration('rviz')), output='screen'),
    ])


## src/vacuum_sim/worlds

## src/vacuum_sim/worlds/room.sdf

<?xml version="1.0"?>
<sdf version="1.9">
  <world name="vacuum_room">
    <physics name="physics" type="ignored"><max_step_size>0.002</max_step_size><real_time_factor>1.0</real_time_factor></physics>
    <gravity>0 0 -9.81</gravity>
    <plugin filename="gz-sim-physics-system" name="gz::sim::systems::Physics"/>
    <plugin filename="gz-sim-user-commands-system" name="gz::sim::systems::UserCommands"/>
    <plugin filename="gz-sim-scene-broadcaster-system" name="gz::sim::systems::SceneBroadcaster"/>
    <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors"><render_engine>ogre2</render_engine></plugin>
    <scene><ambient>0.6 0.6 0.6 1</ambient><background>0.8 0.85 0.9 1</background><shadows>false</shadows></scene>
    <light name="sun" type="directional"><pose>0 0 6 0 0 0</pose><diffuse>0.8 0.8 0.8 1</diffuse><specular>0.2 0.2 0.2 1</specular><direction>-0.5 -0.4 -1</direction><cast_shadows>false</cast_shadows></light>
    <model name="floor"><static>true</static><link name="floor">
      <collision name="collision"><geometry><plane><normal>0 0 1</normal><size>8 8</size></plane></geometry></collision>
      <visual name="visual"><geometry><plane><normal>0 0 1</normal><size>8 8</size></plane></geometry><material><ambient>0.55 0.48 0.38 1</ambient><diffuse>0.65 0.58 0.48 1</diffuse></material></visual>
    </link></model>
    <model name="walls"><static>true</static>
      <link name="north"><pose>0 3 0.5 0 0 0</pose><collision name="c"><geometry><box><size>6.2 0.1 1</size></box></geometry></collision><visual name="v"><geometry><box><size>6.2 0.1 1</size></box></geometry><material><diffuse>0.85 0.87 0.9 1</diffuse></material></visual></link>
      <link name="south"><pose>0 -3 0.5 0 0 0</pose><collision name="c"><geometry><box><size>6.2 0.1 1</size></box></geometry></collision><visual name="v"><geometry><box><size>6.2 0.1 1</size></box></geometry><material><diffuse>0.85 0.87 0.9 1</diffuse></material></visual></link>
      <link name="east"><pose>3 0 0.5 0 0 0</pose><collision name="c"><geometry><box><size>0.1 6 1</size></box></geometry></collision><visual name="v"><geometry><box><size>0.1 6 1</size></box></geometry><material><diffuse>0.85 0.87 0.9 1</diffuse></material></visual></link>
      <link name="west"><pose>-3 0 0.5 0 0 0</pose><collision name="c"><geometry><box><size>0.1 6 1</size></box></geometry></collision><visual name="v"><geometry><box><size>0.1 6 1</size></box></geometry><material><diffuse>0.85 0.87 0.9 1</diffuse></material></visual></link>
    </model>
    <model name="cabinet"><static>true</static><pose>1.3 1.1 0.35 0 0 0</pose><link name="body"><collision name="c"><geometry><box><size>1.0 0.6 0.7</size></box></geometry></collision><visual name="v"><geometry><box><size>1.0 0.6 0.7</size></box></geometry><material><diffuse>0.25 0.40 0.55 1</diffuse></material></visual></link></model>
    <model name="box"><static>true</static><pose>-1.4 -1.1 0.2 0 0 0.3</pose><link name="body"><collision name="c"><geometry><box><size>0.5 0.6 0.4</size></box></geometry></collision><visual name="v"><geometry><box><size>0.5 0.6 0.4</size></box></geometry><material><diffuse>0.7 0.4 0.2 1</diffuse></material></visual></link></model>
  </world>
</sdf>


## src/vacuum_sim/urdf

## src/vacuum_sim/urdf/vacuum.urdf.xacro

<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="vacuum">
  <!-- All geometry and masses are simulation placeholders, not measured specifications.
       Wheel radius/separation must match controllers.yaml until launch-time generation is added. -->
  <xacro:arg name="controllers_file" default="$(find vacuum_sim)/config/controllers.yaml"/>
  <xacro:arg name="camera_width" default="320"/>
  <xacro:arg name="camera_height" default="240"/>
  <xacro:arg name="camera_rate" default="5"/>
  <xacro:property name="wheel_radius" value="0.05"/>
  <xacro:property name="wheel_separation" value="0.29"/>
  <xacro:property name="wheel_width" value="0.025"/>
  <xacro:property name="body_x" value="0.30"/>
  <xacro:property name="body_y" value="0.25"/>
  <xacro:property name="body_z" value="0.10"/>
  <xacro:property name="body_mass" value="3.0"/>
  <material name="acrylic"><color rgba="0.2 0.65 0.85 0.6"/></material>
  <material name="rubber"><color rgba="0.08 0.08 0.10 1"/></material>
  <material name="sensor"><color rgba="0.15 0.18 0.20 1"/></material>

  <link name="base_footprint"/>
  <!-- The axle is ahead of the body center, keeping the center of mass within
       the two-wheel/caster support triangle. base_footprint stays at the axle. -->
  <joint name="base_joint" type="fixed"><parent link="base_footprint"/><child link="base_link"/><origin xyz="-0.05 0 0.08"/></joint>
  <link name="base_link">
    <inertial><mass value="${body_mass}"/><inertia ixx="${body_mass*(body_y**2+body_z**2)/12}" iyy="${body_mass*(body_x**2+body_z**2)/12}" izz="${body_mass*(body_x**2+body_y**2)/12}" ixy="0" ixz="0" iyz="0"/></inertial>
    <collision><geometry><box size="${body_x} ${body_y} ${body_z}"/></geometry></collision>
    <visual><origin xyz="0 0 -0.048"/><geometry><box size="${body_x} ${body_y} 0.004"/></geometry><material name="acrylic"/></visual>
    <visual><origin xyz="0 0 0.048"/><geometry><box size="${body_x} ${body_y} 0.004"/></geometry><material name="acrylic"/></visual>
    <visual><geometry><box size="0.20 0.16 0.065"/></geometry><material name="sensor"/></visual>
  </link>

  <xacro:macro name="wheel" params="side sign">
    <link name="${side}_wheel">
      <inertial><mass value="0.12"/><inertia ixx="${0.12*(3*wheel_radius**2+wheel_width**2)/12}" iyy="${0.12*wheel_radius**2/2}" izz="${0.12*(3*wheel_radius**2+wheel_width**2)/12}" ixy="0" ixz="0" iyz="0"/></inertial>
      <visual><origin rpy="${pi/2} 0 0"/><geometry><cylinder radius="${wheel_radius}" length="${wheel_width}"/></geometry><material name="rubber"/></visual>
      <collision><origin rpy="${pi/2} 0 0"/><geometry><cylinder radius="${wheel_radius}" length="${wheel_width}"/></geometry></collision>
    </link>
    <joint name="${side}_wheel_joint" type="continuous">
      <parent link="base_link"/><child link="${side}_wheel"/>
      <origin xyz="0.05 ${sign*wheel_separation/2} ${wheel_radius-0.08}"/><axis xyz="0 1 0"/>
      <limit effort="3.0" velocity="10.0"/><dynamics damping="0.01" friction="0.0"/>
    </joint>
    <gazebo reference="${side}_wheel"><mu1>1.0</mu1><mu2>1.0</mu2></gazebo>
  </xacro:macro>
  <xacro:wheel side="left" sign="1"/><xacro:wheel side="right" sign="-1"/>

  <!-- A low-friction support sphere approximates a caster, not its swivel mechanics. -->
  <joint name="caster_joint" type="fixed"><parent link="base_link"/><child link="caster"/><origin xyz="-0.115 0 -0.06"/></joint>
  <link name="caster">
    <inertial><mass value="0.08"/><inertia ixx="0.0000128" iyy="0.0000128" izz="0.0000128" ixy="0" ixz="0" iyz="0"/></inertial>
    <visual><geometry><sphere radius="0.02"/></geometry><material name="rubber"/></visual>
    <collision><geometry><sphere radius="0.02"/></geometry></collision>
  </link>
  <gazebo reference="caster_joint"><preserveFixedJoint>true</preserveFixedJoint></gazebo>
  <gazebo reference="caster"><mu1>0.01</mu1><mu2>0.01</mu2></gazebo>

  <joint name="lidar_joint" type="fixed"><parent link="base_link"/><child link="lidar_link"/><origin xyz="0 0 0.085"/></joint>
  <link name="lidar_link">
    <inertial><mass value="0.05"/><inertia ixx="0.00001" iyy="0.00001" izz="0.00002" ixy="0" ixz="0" iyz="0"/></inertial>
    <visual><geometry><cylinder radius="0.03" length="0.025"/></geometry><material name="sensor"/></visual>
    <collision><geometry><cylinder radius="0.03" length="0.025"/></geometry></collision>
  </link>
  <gazebo reference="lidar_joint"><preserveFixedJoint>true</preserveFixedJoint></gazebo>
  <gazebo reference="lidar_link">
    <!-- Generic 2-D lidar. These are not claims about the C1's exact scan specifications. -->
    <sensor name="lidar" type="gpu_lidar">
      <topic>/scan</topic><gz_frame_id>lidar_link</gz_frame_id><update_rate>10</update_rate><always_on>true</always_on>
      <lidar><scan><horizontal><samples>360</samples><resolution>1</resolution><min_angle>${-pi}</min_angle><max_angle>${pi}</max_angle></horizontal></scan>
        <range><min>0.08</min><max>12.0</max><resolution>0.01</resolution></range>
        <noise><type>gaussian</type><mean>0</mean><stddev>0.005</stddev></noise>
      </lidar>
    </sensor>
  </gazebo>

  <joint name="camera_joint" type="fixed"><parent link="base_link"/><child link="camera_link"/><origin xyz="0.155 0 0.025"/></joint>
  <link name="camera_link">
    <inertial><mass value="0.03"/><inertia ixx="0.000004" iyy="0.000004" izz="0.000004" ixy="0" ixz="0" iyz="0"/></inertial>
    <visual><geometry><box size="0.015 0.04 0.025"/></geometry><material name="sensor"/></visual>
  </link>
  <joint name="camera_optical_joint" type="fixed"><parent link="camera_link"/><child link="camera_optical_frame"/><origin rpy="${-pi/2} 0 ${-pi/2}"/></joint>
  <link name="camera_optical_frame"/>
  <gazebo reference="camera_joint"><preserveFixedJoint>true</preserveFixedJoint></gazebo>
  <gazebo reference="camera_link">
    <sensor name="camera" type="camera"><topic>/camera/image_raw</topic><gz_frame_id>camera_optical_frame</gz_frame_id>
      <update_rate>$(arg camera_rate)</update_rate><always_on>true</always_on>
      <camera><horizontal_fov>1.0472</horizontal_fov><image><width>$(arg camera_width)</width><height>$(arg camera_height)</height><format>R8G8B8</format></image><clip><near>0.03</near><far>15</far></clip><camera_info_topic>/camera/camera_info</camera_info_topic></camera>
    </sensor>
  </gazebo>

  <ros2_control name="VacuumSimulation" type="system">
    <hardware><plugin>gz_ros2_control/GazeboSimSystem</plugin></hardware>
    <joint name="left_wheel_joint"><command_interface name="velocity"/><state_interface name="position"/><state_interface name="velocity"/></joint>
    <joint name="right_wheel_joint"><command_interface name="velocity"/><state_interface name="position"/><state_interface name="velocity"/></joint>
  </ros2_control>
  <gazebo>
    <plugin filename="libgz_ros2_control-system.so" name="gz_ros2_control::GazeboSimROS2ControlPlugin">
      <parameters>$(arg controllers_file)</parameters>
      <ros><remapping>/diff_drive_controller/odom:=/odom</remapping></ros>
    </plugin>
  </gazebo>
</robot>


## src/vacuum_sim/scripts

## src/vacuum_sim/scripts/twist_adapter.py

#!/usr/bin/env python3
"""Simulation-only adapter for Jazzy's unstamped teleop/Nav2 Twist messages.

Publishes only on receipt. The diff-drive controller enforces its 0.5 s timeout.
This module does not implement an emergency stop for a physical robot.
"""
import math
import rclpy
from geometry_msgs.msg import Twist, TwistStamped
from rclpy.node import Node


class TwistAdapter(Node):
    def __init__(self):
        super().__init__('simulation_twist_adapter')
        self.publisher = self.create_publisher(TwistStamped, '/diff_drive_controller/cmd_vel', 10)
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.on_twist, 10)

    def on_twist(self, message):
        outgoing = TwistStamped()
        outgoing.header.stamp = self.get_clock().now().to_msg()
        outgoing.header.frame_id = 'base_footprint'
        if math.isfinite(message.linear.x) and math.isfinite(message.angular.z):
            outgoing.twist.linear.x = max(-0.15, min(0.25, message.linear.x))
            outgoing.twist.angular.z = max(-1.0, min(1.0, message.angular.z))
        self.publisher.publish(outgoing)


def main():
    rclpy.init()
    node = TwistAdapter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()


## src/vacuum_sim/CMakeLists.txt

cmake_minimum_required(VERSION 3.8)
project(vacuum_sim)
find_package(ament_cmake REQUIRED)
install(DIRECTORY urdf config launch worlds DESTINATION share/${PROJECT_NAME})
install(PROGRAMS scripts/twist_adapter.py DESTINATION lib/${PROJECT_NAME})
ament_package()


## tools

## tools/run_sim.py

#!/usr/bin/env python3
"""Launch one local simulation and clean up its own processes on exit."""
import fcntl
import os
from pathlib import Path
import signal
import subprocess
import sys

workspace = Path(__file__).resolve().parents[1]
lock = (workspace / '.simulator.lock').open('a')
try:
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError:
    raise SystemExit('This workspace already has a simulator running. Stop its terminal first.')

def interrupted(signum, frame):
    raise KeyboardInterrupt

signal.signal(signal.SIGTERM, interrupted)
process = subprocess.Popen(['/bin/bash', '-lc', 'source env.sh; exec "$@"', 'vacuum-launch',
                            'ros2', 'launch', 'vacuum_sim', 'sim.launch.py', *sys.argv[1:]],
                           cwd=workspace, start_new_session=True)
result = 0
try:
    result = process.wait()
except KeyboardInterrupt:
    result = 130
finally:
    try:
        os.killpg(process.pid, signal.SIGINT)
        process.wait(timeout=8)
    except subprocess.TimeoutExpired:
        pass
    except ProcessLookupError:
        pass
    try:
        os.killpg(process.pid, signal.SIGTERM)
        process.wait(timeout=3)
    except (ProcessLookupError, subprocess.TimeoutExpired):
        pass
    lock.close()
sys.exit(result)


## tools/prepare_nav2.py

#!/usr/bin/env python3
"""Adapt the installed Jazzy Nav2 defaults; run in Ubuntu before colcon build.

Keeping defaults from the installed package avoids inventing plugin names or
dropping lifecycle nodes introduced in package updates. Review the generated YAML.
"""
from pathlib import Path
import yaml

workspace = Path(__file__).resolve().parents[1]
source = Path('/opt/ros/jazzy/share/nav2_bringup/params/nav2_params.yaml')
target = workspace / 'src/vacuum_sim/config/nav2.yaml'
if target.exists():
    raise SystemExit(f'{target} already exists; preserve and review existing configuration.')
data = yaml.safe_load(source.read_text())


def set_sim_time(value):
    if isinstance(value, dict):
        if 'ros__parameters' in value:
            value['ros__parameters']['use_sim_time'] = True
        for item in value.values():
            set_sim_time(item)


set_sim_time(data)
for name in ('bt_navigator', 'behavior_server'):
    params = data[name]['ros__parameters']
    params['robot_base_frame'] = 'base_footprint'
    params['odom_topic'] = '/odom'
    params['enable_stamped_cmd_vel'] = False

for name in ('local_costmap', 'global_costmap'):
    params = data[name][name]['ros__parameters']
    params['robot_base_frame'] = 'base_footprint'
    params['robot_radius'] = 0.22
    params.pop('footprint', None)
    params['resolution'] = 0.05
    params['inflation_layer']['inflation_radius'] = 0.35
    for layer in ('voxel_layer', 'obstacle_layer'):
        if layer in params and 'scan' in params[layer]:
            params[layer]['scan'].update(topic='/scan', data_type='LaserScan',
                                        obstacle_max_range=6.0, raytrace_max_range=8.0)

controller = data['controller_server']['ros__parameters']
controller['controller_frequency'] = 20.0
controller['odom_topic'] = '/odom'
controller['enable_stamped_cmd_vel'] = False
controller['progress_checker'].update(required_movement_radius=0.15, movement_time_allowance=30.0)
controller['general_goal_checker'].update(xy_goal_tolerance=0.15, yaw_goal_tolerance=0.25)
controller['controller_plugins'] = ['FollowPath']
controller['FollowPath'] = {
    'plugin': 'dwb_core::DWBLocalPlanner',
    'debug_trajectory_details': False,
    'min_vel_x': -0.15, 'max_vel_x': 0.25,
    'min_vel_y': 0.0, 'max_vel_y': 0.0,
    'max_vel_theta': 1.0,
    'min_speed_xy': 0.0, 'max_speed_xy': 0.25, 'min_speed_theta': 0.0,
    'acc_lim_x': 0.3, 'acc_lim_y': 0.0, 'acc_lim_theta': 1.0,
    'decel_lim_x': -0.3, 'decel_lim_y': 0.0, 'decel_lim_theta': -1.0,
    'vx_samples': 20, 'vy_samples': 1, 'vtheta_samples': 20,
    'sim_time': 1.7, 'linear_granularity': 0.05, 'angular_granularity': 0.025,
    'transform_tolerance': 0.2, 'xy_goal_tolerance': 0.15,
    'trans_stopped_velocity': 0.02, 'short_circuit_trajectory_evaluation': True,
    'stateful': True,
    'critics': ['RotateToGoal', 'Oscillation', 'BaseObstacle', 'GoalAlign', 'PathAlign', 'PathDist', 'GoalDist'],
    'BaseObstacle.scale': 0.02,
    'PathAlign.scale': 32.0, 'PathAlign.forward_point_distance': 0.1,
    'GoalAlign.scale': 24.0, 'GoalAlign.forward_point_distance': 0.1,
    'PathDist.scale': 32.0, 'GoalDist.scale': 24.0,
    'RotateToGoal.scale': 32.0, 'RotateToGoal.slowing_factor': 5.0,
    'RotateToGoal.lookahead_time': -1.0,
}
if 'velocity_smoother' in data:
    data['velocity_smoother']['ros__parameters'].update(
        enable_stamped_cmd_vel=False,
        max_velocity=[0.25, 0.0, 1.0], min_velocity=[-0.15, 0.0, -1.0],
        max_accel=[0.3, 0.0, 1.0], max_decel=[-0.3, 0.0, -1.0],
        odom_topic='/odom', feedback='OPEN_LOOP', velocity_timeout=0.5)
if 'collision_monitor' in data:
    data['collision_monitor']['ros__parameters'].update(enable_stamped_cmd_vel=False,
        base_frame_id='base_footprint', cmd_vel_in_topic='cmd_vel_smoothed', cmd_vel_out_topic='cmd_vel')
if 'docking_server' in data:
    data['docking_server']['ros__parameters'].update(enable_stamped_cmd_vel=False, base_frame='base_footprint')
data['planner_server']['ros__parameters']['GridBased']['allow_unknown'] = False
target.write_text(yaml.safe_dump(data, sort_keys=False))
print(f'Prepared {target}; navigation runtime validation remains required.')


## env.sh

#!/usr/bin/env bash
# Source from each development terminal. Intended exclusively for local simulation.
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
export ROS_DOMAIN_ID=42
export GZ_PARTITION=vacuum_sim_42
export GZ_IP=127.0.0.1
# Verified WSLg hardware rendering on this PC. Applies only to this workspace.
export GALLIUM_DRIVER=d3d12
export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA
source /opt/ros/jazzy/setup.bash
vacuum_workspace="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$vacuum_workspace/install/setup.bash" ]]; then
  source "$vacuum_workspace/install/setup.bash"
fi
unset vacuum_workspace


## README.md

# Your Windows + Ubuntu robot environment

Windows remains your operating system. Ubuntu runs in WSL 2, with Linux programs opening their own graphical windows through WSLg. You do not need to dual boot.

## Start here

1. Double-click **Vacuum Simulator.cmd** to open Gazebo and RViz with the example vacuum robot. Keep its terminal open. Wait for both wheel controllers to become active.
2. Double-click **Ubuntu Terminal.cmd** for a Linux shell. Your Linux username is `robot`; `sudo` uses the private password you set. Password typing is invisible.
3. Double-click **Robot Code.cmd** to open `/home/robot/vacuum_ws` in VS Code through WSL. Choose **WSL: VacuumRobot-24.04** if VS Code asks which environment to use.

Use the commands below **inside Ubuntu**, not in a Windows PowerShell prompt. In each new terminal:

```bash
cd ~/vacuum_ws
source env.sh
```

## Drive the simulation

The default settings now reduce rendering load: camera **320 × 240 at 5 Hz**, RViz **15 frames/s**, and scene shadows disabled. Physics, drive control and the lidar configuration are unchanged. Original source configuration files are preserved at `~/vacuum_ws/performance-originals`; the full export on F: contains the original settings.

If the two graphical windows still feel slow, stop the current simulation first and use **Vacuum Simulator - RViz only.cmd**. Gazebo then runs the simulation without its separate 3D window, while RViz remains available for the robot, lidar, map and camera.

To request the original camera resolution/rate, start from an Ubuntu terminal:

```bash
ros2 launch vacuum_sim sim.launch.py camera_width:=640 camera_height:=480 camera_rate:=10
```

This increases rendering and image-transfer work. Only run one simulator instance at a time.

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p speed:=0.15 -p turn:=0.5
```

Focus the teleoperation terminal. `i` moves forward, `j` turns left, `l` turns right, `,` reverses, and `k` stops. Read the help printed by the program. The adapter clamps commands to 0.25 m/s forward, 0.15 m/s reverse and 1 rad/s rotation. The simulated drive controller stops when commands expire after 0.5 seconds; it also limits acceleration.

Only run one movement command source at a time. Stop teleoperation before starting autonomous navigation.

## Mapping and navigation

With the simulator running, start a second Ubuntu terminal:

```bash
cd ~/vacuum_ws
source env.sh
ros2 launch vacuum_sim mapping.launch.py
```

Drive slowly around the room to build a lidar map. RViz displays `/map`, `/scan`, the robot and camera image. For navigation, start another terminal:

```bash
cd ~/vacuum_ws
source env.sh
ros2 launch vacuum_sim navigation.launch.py
```

Keep mapping running. In RViz, set **Global Options → Fixed Frame** to `map`, choose **Nav2 Goal**, then click and drag a destination arrow in observed free space. This example navigates using the live SLAM map.

Save a map with:

```bash
mkdir -p ~/vacuum_ws/maps
ros2 run nav2_map_server map_saver_cli -f ~/vacuum_ws/maps/room --ros-args -p use_sim_time:=true
```

A saved map is data; this live-mapping launch does not automatically load it. AMCL localization and saved-map startup can be configured when your world and robot geometry are ready.

## Edit and rebuild

The workspace is in Ubuntu's filesystem for good Linux build performance. Windows Explorer can reach it at `\\wsl.localhost\VacuumRobot-24.04\home\robot\vacuum_ws`.

Key files are `src/vacuum_sim/urdf/vacuum.urdf.xacro` (body/sensors), `config/controllers.yaml` (drive geometry/limits), `config/nav2.yaml` (navigation), and `worlds/room.sdf` (room).

Wheel radius and separation must match in the URDF and controller configuration. The starting values are **50 mm wheel radius**, **290 mm wheel separation**, and a **300 × 250 mm** body. Body mass, caster behavior, inertias and sensor properties are placeholders. Replace them with measured dimensions and specifications.

```bash
cd ~/vacuum_ws
source env.sh
colcon build --symlink-install
source env.sh
```

Stop and restart the simulator after editing geometry or controller configuration. Build errors should be fixed before restarting.

## Stop and resume safely

Press **Ctrl+C** in teleoperation/navigation first, then mapping, then the simulator terminal. Wait for processes to exit. Windows PowerShell can stop this specific Ubuntu instance using:

```powershell
wsl --terminate VacuumRobot-24.04
```

Restart using the launchers. Do not use `wsl --unregister`: it deletes the Linux environment.

## Storage and isolation

Ubuntu is stored at `E:\WSL\VacuumRobot\Ubuntu-24.04`. The virtual disk grows as files are written, up to 40 GB. WSL is capped at 10 GB RAM, six processors, and 2 GB swap. These resource settings apply to all WSL 2 distributions on this Windows account. Keep free space on E: for disk growth.

`env.sh` uses ROS domain 42, localhost discovery, and a dedicated local Gazebo transport partition. These prevent accidental ROS discovery of other computers in the normal setup; WSL still has Internet access. No robot USB devices are attached or flashed, no robot motor commands are sent, and no Windows firewall rules have been opened.

## Backup

The full Ubuntu export is in `F:\VacuumRobotBackups`; its exact filename and SHA-256 are recorded in `backup-verification.json` beside this guide. Keep F: connected when accessing that backup. The export includes Linux programs, robot code, and Linux account settings; keep it private. Archive structure and checksum were checked; a separate restore-and-boot test was not performed.

If restoration is needed, use a **new distribution name and an empty storage location**. For example, in Windows PowerShell, replace `FULL_BACKUP_PATH` with the path in the verification file:

```powershell
wsl --import VacuumRobot-Restored E:\WSL\VacuumRobot-Restored "FULL_BACKUP_PATH" --version 2
wsl --manage VacuumRobot-Restored --set-default-user robot
wsl -d VacuumRobot-Restored -u robot --cd /home/robot/vacuum_ws
```

This preserves the current distribution. Run only one copy of the example simulator at a time. The launchers target `VacuumRobot-24.04`; change their distribution name if using a restored copy. There is also a small `vacuum-workspace-source.tar.gz` beside this guide containing the starter source and example saved map.

## Moving toward your physical vacuum

- **Orange Pi 5:** run the onboard ROS 2 stack on a compatible Ubuntu 24.04 ARM64 image, after checking its board kernel, camera and serial support. WSL is your PC development/simulation environment.
- **RPLIDAR C1:** add and test Slamtec's C1 driver on the actual Linux board. This simulation uses a generic 360-sample lidar and does not certify C1 performance.
- **Arduino Mega:** use ordinary firmware and a serial ROS bridge. The Mega is not a supported target of `micro_ros_arduino`; it should not run the full ROS stack.
- **NEMA 17 drive:** motor model, driver, gearing, wheel size and encoder feedback still need to be specified. The simulation assumes ideal velocity-controlled wheels and does not model lost steps, electrical current or motor torque limits.
- **Acrylic plates/camera:** measure plate dimensions, thickness, mass and sensor mounts. Simulation does not establish chassis strength, suction performance, battery safety or camera driver compatibility.

Before driving hardware, add a physical emergency stop, an onboard command watchdog, motor/current limits, and independent tests with the wheels lifted. Those hardware protections are separate from this simulator's timeout.

Official references: [ROS 2 Jazzy](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html), [Gazebo Harmonic with ROS](https://gazebosim.org/docs/harmonic/ros_installation/), [WSLg GUI applications](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps), [Slamtec ROS 2 driver](https://github.com/Slamtec/sllidar_ros2), [micro-ROS Arduino supported boards](https://github.com/micro-ROS/micro_ros_arduino).


## maps

## maps/room.pgm

## maps/room.yaml

image: room.pgm
mode: trinary
resolution: 0.050
origin: [-2.966, -2.974, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## performance-originals

## performance-originals/config

## performance-originals/config/view.rviz

Panels:
  - Class: rviz_common/Displays
    Help Height: 70
    Name: Displays
    Property Tree Widget:
      Expanded: ~
      Splitter Ratio: 0.5
    Tree Height: 208
  - Class: rviz_common/Tool Properties
    Expanded: ~
    Name: Tool Properties
    Splitter Ratio: 0.5
Visualization Manager:
  Class: ""
  Displays:
    - Alpha: 0.5
      Cell Size: 0.5
      Class: rviz_default_plugins/Grid
      Color: 160; 160; 164
      Enabled: true
      Line Style:
        Line Width: 0.029999999329447746
        Value: Lines
      Name: Grid
      Normal Cell Count: 0
      Offset:
        X: 0
        Y: 0
        Z: 0
      Plane: XY
      Plane Cell Count: 20
      Reference Frame: <Fixed Frame>
      Value: true
    - Alpha: 1
      Class: rviz_default_plugins/RobotModel
      Collision Enabled: false
      Description File: ""
      Description Source: Topic
      Description Topic:
        Depth: 5
        Durability Policy: Transient Local
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /robot_description
      Enabled: true
      Links:
        All Links Enabled: true
        Expand Joint Details: false
        Expand Link Details: false
        Expand Tree: false
        Link Tree Style: Links in Alphabetic Order
        base_footprint:
          Alpha: 1
          Show Axes: false
          Show Trail: false
        base_link:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        camera_link:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        camera_optical_frame:
          Alpha: 1
          Show Axes: false
          Show Trail: false
        caster:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        left_wheel:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        lidar_link:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
        right_wheel:
          Alpha: 1
          Show Axes: false
          Show Trail: false
          Value: true
      Mass Properties:
        Inertia: false
        Mass: false
      Name: Robot
      TF Prefix: ""
      Update Interval: 0
      Value: true
      Visual Enabled: true
    - Alpha: 1
      Autocompute Intensity Bounds: true
      Autocompute Value Bounds:
        Max Value: 10
        Min Value: -10
        Value: true
      Axis: Z
      Channel Name: intensity
      Class: rviz_default_plugins/LaserScan
      Color: 255; 255; 255
      Color Transformer: Intensity
      Decay Time: 0
      Enabled: true
      Invert Rainbow: false
      Max Color: 255; 255; 255
      Max Intensity: 0
      Min Color: 0; 0; 0
      Min Intensity: 0
      Name: Lidar
      Position Transformer: XYZ
      Selectable: true
      Size (Pixels): 3
      Size (m): 0.02500000037252903
      Style: Flat Squares
      Topic:
        Depth: 5
        Durability Policy: Volatile
        Filter size: 10
        History Policy: Keep Last
        Reliability Policy: Best Effort
        Value: /scan
      Use Fixed Frame: true
      Use rainbow: true
      Value: true
    - Alpha: 0.699999988079071
      Binary representation: false
      Binary threshold: 100
      Class: rviz_default_plugins/Map
      Color Scheme: map
      Draw Behind: false
      Enabled: true
      Name: Map
      Topic:
        Depth: 5
        Durability Policy: Transient Local
        Filter size: 10
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /map
      Update Topic:
        Depth: 5
        Durability Policy: Volatile
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /map_updates
      Use Timestamp: false
      Value: true
    - Class: rviz_default_plugins/Image
      Enabled: true
      Max Value: 1
      Median window: 5
      Min Value: 0
      Name: Camera
      Normalize Range: true
      Topic:
        Depth: 5
        Durability Policy: Volatile
        History Policy: Keep Last
        Reliability Policy: Best Effort
        Value: /camera/image_raw
      Value: true
  Enabled: true
  Global Options:
    Background Color: 35; 40; 48
    Fixed Frame: odom
    Frame Rate: 30
  Name: root
  Tools:
    - Class: rviz_default_plugins/Interact
      Hide Inactive Objects: true
    - Class: rviz_default_plugins/MoveCamera
    - Class: rviz_default_plugins/Select
    - Class: nav2_rviz_plugins/GoalTool
  Transformation:
    Current:
      Class: rviz_default_plugins/TF
  Value: true
  Views:
    Current:
      Class: rviz_default_plugins/Orbit
      Distance: 6
      Enable Stereo Rendering:
        Stereo Eye Separation: 0.05999999865889549
        Stereo Focal Distance: 1
        Swap Stereo Eyes: false
        Value: false
      Focal Point:
        X: 0
        Y: 0
        Z: 0
      Focal Shape Fixed Size: true
      Focal Shape Size: 0.05000000074505806
      Invert Z Axis: false
      Name: Current View
      Near Clip Distance: 0.009999999776482582
      Pitch: 0.800000011920929
      Target Frame: <Fixed Frame>
      Value: Orbit (rviz_default_plugins)
      Yaw: 0.800000011920929
    Saved: ~
Window Geometry:
  Camera:
    collapsed: false
  Displays:
    collapsed: false
  Height: 800
  Hide Left Dock: false
  Hide Right Dock: false
  QMainWindow State: 000000ff00000000fd000000010000000000000156000002cafc0200000003fb0000000c00430061006d006500720061010000003b000000c90000001600fffffffb000000100044006900730070006c006100790073010000010a00000151000000c700fffffffb0000001e0054006f006f006c002000500072006f00700065007200740069006500730100000261000000a40000005c00ffffff00000354000002ca00000004000000040000000800000008fc0000000100000002000000010000000a0054006f006f006c00730100000000ffffffff0000000000000000
  Tool Properties:
    collapsed: false
  Width: 1200
  X: 1934
  Y: 40


## performance-originals/launch

## performance-originals/launch/sim.launch.py

from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler, SetEnvironmentVariable
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    gz_launch = str(Path(get_package_share_directory('ros_gz_sim')) / 'launch' / 'gz_sim.launch.py')
    description = ParameterValue(Command(['xacro ', str(package / 'urdf/vacuum.urdf.xacro')]), value_type=str)
    spawn = Node(package='ros_gz_sim', executable='create', arguments=[
        '-world', 'vacuum_room', '-name', 'vacuum', '-topic', '/robot_description', '-z', '0.015'], output='screen')
    controllers = Node(package='controller_manager', executable='spawner', arguments=[
        'joint_state_broadcaster', 'diff_drive_controller', '--controller-manager-timeout', '120'], output='screen')
    return LaunchDescription([
        DeclareLaunchArgument('gui', default_value='true'),
        DeclareLaunchArgument('rviz', default_value='true'),
        SetEnvironmentVariable('ROS_AUTOMATIC_DISCOVERY_RANGE', 'LOCALHOST'),
        SetEnvironmentVariable('ROS_DOMAIN_ID', '42'),
        SetEnvironmentVariable('GZ_PARTITION', 'vacuum_sim_42'),
        SetEnvironmentVariable('GZ_IP', '127.0.0.1'),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(gz_launch), launch_arguments={
            'gz_args': '-r -s -v 3 ' + str(package / 'worlds/room.sdf')}.items()),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(gz_launch), launch_arguments={
            'gz_args': '-g -v 3'}.items(), condition=IfCondition(LaunchConfiguration('gui'))),
        Node(package='robot_state_publisher', executable='robot_state_publisher',
             parameters=[{'robot_description': description, 'use_sim_time': True}], output='screen'),
        Node(package='ros_gz_bridge', executable='parameter_bridge', parameters=[
            {'config_file': str(package / 'config/bridge.yaml'), 'use_sim_time': True}], output='screen'),
        RegisterEventHandler(OnProcessExit(target_action=spawn, on_exit=[controllers])),
        spawn,
        Node(package='vacuum_sim', executable='twist_adapter.py', parameters=[{'use_sim_time': True}], output='screen'),
        Node(package='rviz2', executable='rviz2', arguments=['-d', str(package / 'config/view.rviz')],
             parameters=[{'use_sim_time': True}], condition=IfCondition(LaunchConfiguration('rviz')), output='screen'),
    ])


## performance-originals/worlds

## performance-originals/worlds/room.sdf

<?xml version="1.0"?>
<sdf version="1.9">
  <world name="vacuum_room">
    <physics name="physics" type="ignored"><max_step_size>0.002</max_step_size><real_time_factor>1.0</real_time_factor></physics>
    <gravity>0 0 -9.81</gravity>
    <plugin filename="gz-sim-physics-system" name="gz::sim::systems::Physics"/>
    <plugin filename="gz-sim-user-commands-system" name="gz::sim::systems::UserCommands"/>
    <plugin filename="gz-sim-scene-broadcaster-system" name="gz::sim::systems::SceneBroadcaster"/>
    <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors"><render_engine>ogre2</render_engine></plugin>
    <scene><ambient>0.6 0.6 0.6 1</ambient><background>0.8 0.85 0.9 1</background><shadows>true</shadows></scene>
    <light name="sun" type="directional"><pose>0 0 6 0 0 0</pose><diffuse>0.8 0.8 0.8 1</diffuse><specular>0.2 0.2 0.2 1</specular><direction>-0.5 -0.4 -1</direction><cast_shadows>true</cast_shadows></light>
    <model name="floor"><static>true</static><link name="floor">
      <collision name="collision"><geometry><plane><normal>0 0 1</normal><size>8 8</size></plane></geometry></collision>
      <visual name="visual"><geometry><plane><normal>0 0 1</normal><size>8 8</size></plane></geometry><material><ambient>0.55 0.48 0.38 1</ambient><diffuse>0.65 0.58 0.48 1</diffuse></material></visual>
    </link></model>
    <model name="walls"><static>true</static>
      <link name="north"><pose>0 3 0.5 0 0 0</pose><collision name="c"><geometry><box><size>6.2 0.1 1</size></box></geometry></collision><visual name="v"><geometry><box><size>6.2 0.1 1</size></box></geometry><material><diffuse>0.85 0.87 0.9 1</diffuse></material></visual></link>
      <link name="south"><pose>0 -3 0.5 0 0 0</pose><collision name="c"><geometry><box><size>6.2 0.1 1</size></box></geometry></collision><visual name="v"><geometry><box><size>6.2 0.1 1</size></box></geometry><material><diffuse>0.85 0.87 0.9 1</diffuse></material></visual></link>
      <link name="east"><pose>3 0 0.5 0 0 0</pose><collision name="c"><geometry><box><size>0.1 6 1</size></box></geometry></collision><visual name="v"><geometry><box><size>0.1 6 1</size></box></geometry><material><diffuse>0.85 0.87 0.9 1</diffuse></material></visual></link>
      <link name="west"><pose>-3 0 0.5 0 0 0</pose><collision name="c"><geometry><box><size>0.1 6 1</size></box></geometry></collision><visual name="v"><geometry><box><size>0.1 6 1</size></box></geometry><material><diffuse>0.85 0.87 0.9 1</diffuse></material></visual></link>
    </model>
    <model name="cabinet"><static>true</static><pose>1.3 1.1 0.35 0 0 0</pose><link name="body"><collision name="c"><geometry><box><size>1.0 0.6 0.7</size></box></geometry></collision><visual name="v"><geometry><box><size>1.0 0.6 0.7</size></box></geometry><material><diffuse>0.25 0.40 0.55 1</diffuse></material></visual></link></model>
    <model name="box"><static>true</static><pose>-1.4 -1.1 0.2 0 0 0.3</pose><link name="body"><collision name="c"><geometry><box><size>0.5 0.6 0.4</size></box></geometry></collision><visual name="v"><geometry><box><size>0.5 0.6 0.4</size></box></geometry><material><diffuse>0.7 0.4 0.2 1</diffuse></material></visual></link></model>
  </world>
</sdf>


## performance-originals/urdf

## performance-originals/urdf/vacuum.urdf.xacro

<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="vacuum">
  <!-- All geometry and masses are simulation placeholders, not measured specifications.
       Wheel radius/separation must match controllers.yaml until launch-time generation is added. -->
  <xacro:arg name="controllers_file" default="$(find vacuum_sim)/config/controllers.yaml"/>
  <xacro:property name="wheel_radius" value="0.05"/>
  <xacro:property name="wheel_separation" value="0.29"/>
  <xacro:property name="wheel_width" value="0.025"/>
  <xacro:property name="body_x" value="0.30"/>
  <xacro:property name="body_y" value="0.25"/>
  <xacro:property name="body_z" value="0.10"/>
  <xacro:property name="body_mass" value="3.0"/>
  <material name="acrylic"><color rgba="0.2 0.65 0.85 0.6"/></material>
  <material name="rubber"><color rgba="0.08 0.08 0.10 1"/></material>
  <material name="sensor"><color rgba="0.15 0.18 0.20 1"/></material>

  <link name="base_footprint"/>
  <!-- The axle is ahead of the body center, keeping the center of mass within
       the two-wheel/caster support triangle. base_footprint stays at the axle. -->
  <joint name="base_joint" type="fixed"><parent link="base_footprint"/><child link="base_link"/><origin xyz="-0.05 0 0.08"/></joint>
  <link name="base_link">
    <inertial><mass value="${body_mass}"/><inertia ixx="${body_mass*(body_y**2+body_z**2)/12}" iyy="${body_mass*(body_x**2+body_z**2)/12}" izz="${body_mass*(body_x**2+body_y**2)/12}" ixy="0" ixz="0" iyz="0"/></inertial>
    <collision><geometry><box size="${body_x} ${body_y} ${body_z}"/></geometry></collision>
    <visual><origin xyz="0 0 -0.048"/><geometry><box size="${body_x} ${body_y} 0.004"/></geometry><material name="acrylic"/></visual>
    <visual><origin xyz="0 0 0.048"/><geometry><box size="${body_x} ${body_y} 0.004"/></geometry><material name="acrylic"/></visual>
    <visual><geometry><box size="0.20 0.16 0.065"/></geometry><material name="sensor"/></visual>
  </link>

  <xacro:macro name="wheel" params="side sign">
    <link name="${side}_wheel">
      <inertial><mass value="0.12"/><inertia ixx="${0.12*(3*wheel_radius**2+wheel_width**2)/12}" iyy="${0.12*wheel_radius**2/2}" izz="${0.12*(3*wheel_radius**2+wheel_width**2)/12}" ixy="0" ixz="0" iyz="0"/></inertial>
      <visual><origin rpy="${pi/2} 0 0"/><geometry><cylinder radius="${wheel_radius}" length="${wheel_width}"/></geometry><material name="rubber"/></visual>
      <collision><origin rpy="${pi/2} 0 0"/><geometry><cylinder radius="${wheel_radius}" length="${wheel_width}"/></geometry></collision>
    </link>
    <joint name="${side}_wheel_joint" type="continuous">
      <parent link="base_link"/><child link="${side}_wheel"/>
      <origin xyz="0.05 ${sign*wheel_separation/2} ${wheel_radius-0.08}"/><axis xyz="0 1 0"/>
      <limit effort="3.0" velocity="10.0"/><dynamics damping="0.01" friction="0.0"/>
    </joint>
    <gazebo reference="${side}_wheel"><mu1>1.0</mu1><mu2>1.0</mu2></gazebo>
  </xacro:macro>
  <xacro:wheel side="left" sign="1"/><xacro:wheel side="right" sign="-1"/>

  <!-- A low-friction support sphere approximates a caster, not its swivel mechanics. -->
  <joint name="caster_joint" type="fixed"><parent link="base_link"/><child link="caster"/><origin xyz="-0.115 0 -0.06"/></joint>
  <link name="caster">
    <inertial><mass value="0.08"/><inertia ixx="0.0000128" iyy="0.0000128" izz="0.0000128" ixy="0" ixz="0" iyz="0"/></inertial>
    <visual><geometry><sphere radius="0.02"/></geometry><material name="rubber"/></visual>
    <collision><geometry><sphere radius="0.02"/></geometry></collision>
  </link>
  <gazebo reference="caster_joint"><preserveFixedJoint>true</preserveFixedJoint></gazebo>
  <gazebo reference="caster"><mu1>0.01</mu1><mu2>0.01</mu2></gazebo>

  <joint name="lidar_joint" type="fixed"><parent link="base_link"/><child link="lidar_link"/><origin xyz="0 0 0.085"/></joint>
  <link name="lidar_link">
    <inertial><mass value="0.05"/><inertia ixx="0.00001" iyy="0.00001" izz="0.00002" ixy="0" ixz="0" iyz="0"/></inertial>
    <visual><geometry><cylinder radius="0.03" length="0.025"/></geometry><material name="sensor"/></visual>
    <collision><geometry><cylinder radius="0.03" length="0.025"/></geometry></collision>
  </link>
  <gazebo reference="lidar_joint"><preserveFixedJoint>true</preserveFixedJoint></gazebo>
  <gazebo reference="lidar_link">
    <!-- Generic 2-D lidar. These are not claims about the C1's exact scan specifications. -->
    <sensor name="lidar" type="gpu_lidar">
      <topic>/scan</topic><gz_frame_id>lidar_link</gz_frame_id><update_rate>10</update_rate><always_on>true</always_on>
      <lidar><scan><horizontal><samples>360</samples><resolution>1</resolution><min_angle>${-pi}</min_angle><max_angle>${pi}</max_angle></horizontal></scan>
        <range><min>0.08</min><max>12.0</max><resolution>0.01</resolution></range>
        <noise><type>gaussian</type><mean>0</mean><stddev>0.005</stddev></noise>
      </lidar>
    </sensor>
  </gazebo>

  <joint name="camera_joint" type="fixed"><parent link="base_link"/><child link="camera_link"/><origin xyz="0.155 0 0.025"/></joint>
  <link name="camera_link">
    <inertial><mass value="0.03"/><inertia ixx="0.000004" iyy="0.000004" izz="0.000004" ixy="0" ixz="0" iyz="0"/></inertial>
    <visual><geometry><box size="0.015 0.04 0.025"/></geometry><material name="sensor"/></visual>
  </link>
  <joint name="camera_optical_joint" type="fixed"><parent link="camera_link"/><child link="camera_optical_frame"/><origin rpy="${-pi/2} 0 ${-pi/2}"/></joint>
  <link name="camera_optical_frame"/>
  <gazebo reference="camera_joint"><preserveFixedJoint>true</preserveFixedJoint></gazebo>
  <gazebo reference="camera_link">
    <sensor name="camera" type="camera"><topic>/camera/image_raw</topic><gz_frame_id>camera_optical_frame</gz_frame_id>
      <update_rate>10</update_rate><always_on>true</always_on>
      <camera><horizontal_fov>1.0472</horizontal_fov><image><width>640</width><height>480</height><format>R8G8B8</format></image><clip><near>0.03</near><far>15</far></clip><camera_info_topic>/camera/camera_info</camera_info_topic></camera>
    </sensor>
  </gazebo>

  <ros2_control name="VacuumSimulation" type="system">
    <hardware><plugin>gz_ros2_control/GazeboSimSystem</plugin></hardware>
    <joint name="left_wheel_joint"><command_interface name="velocity"/><state_interface name="position"/><state_interface name="velocity"/></joint>
    <joint name="right_wheel_joint"><command_interface name="velocity"/><state_interface name="position"/><state_interface name="velocity"/></joint>
  </ros2_control>
  <gazebo>
    <plugin filename="libgz_ros2_control-system.so" name="gz_ros2_control::GazeboSimROS2ControlPlugin">
      <parameters>$(arg controllers_file)</parameters>
      <ros><remapping>/diff_drive_controller/odom:=/odom</remapping></ros>
    </plugin>
  </gazebo>
</robot>


## performance-check.json

{
  "baseline_real_time_factor": 0.7747647821972173,
  "tuned_real_time_factor": 0.9058861310192173
}


## simulation-check.json

{
  "counts": {
    "scan": 183,
    "odom": 549,
    "camera_info": 92,
    "image": 91
  },
  "distance_m": 0.5430839999207747,
  "stopped_linear_m_s": 3.764349908134548e-17,
  "stopped_yaw_rad_s": 1.9721522630525296e-32,
  "scan_samples": 360,
  "finite_scan_samples": 360,
  "scan_frame": "lidar_link",
  "image_frame": "camera_optical_frame",
  "image_size": [
    320,
    240
  ],
  "camera_info_frame": "camera_optical_frame"
}


## navigation-check.json

{
  "map_width": 119,
  "map_height": 119,
  "known_cells": 1504,
  "occupied_cells": 36,
  "goal": [
    1.0,
    0.0
  ],
  "status": 4,
  "error_code": 0
}
