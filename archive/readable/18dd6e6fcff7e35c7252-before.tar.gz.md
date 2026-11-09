# before.tar.gz

Historical source: wsl-live


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
    Expanded: null
    Splitter Ratio: 0.5
  Tree Height: 208
- Class: rviz_common/Tool Properties
  Expanded: null
  Name: Tool Properties
  Splitter Ratio: 0.5
Visualization Manager:
  Class: ''
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
    Description File: ''
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
    TF Prefix: ''
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
    Fixed Frame: map
    Frame Rate: 60
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
    Saved: null
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
      footprint: '[[0.120726, 0.0], [0.11783, 0.029405], [0.109252, 0.05768], [0.095324,
        0.083739], [0.076579, 0.106579], [0.053739, 0.125324], [0.02768, 0.139252],
        [-0.000595, 0.14783], [-0.03, 0.150726], [-0.059405, 0.14783], [-0.08768,
        0.139252], [-0.113739, 0.125324], [-0.136579, 0.106579], [-0.155324, 0.083739],
        [-0.169252, 0.05768], [-0.17783, 0.029405], [-0.180726, 0.0], [-0.17783, -0.029405],
        [-0.169252, -0.05768], [-0.155324, -0.083739], [-0.136579, -0.106579], [-0.113739,
        -0.125324], [-0.08768, -0.139252], [-0.059405, -0.14783], [-0.03, -0.150726],
        [-0.000595, -0.14783], [0.02768, -0.139252], [0.053739, -0.125324], [0.076579,
        -0.106579], [0.095324, -0.083739], [0.109252, -0.05768], [0.11783, -0.029405]]'
      footprint_padding: 0.02
global_costmap:
  global_costmap:
    ros__parameters:
      update_frequency: 1.0
      publish_frequency: 1.0
      global_frame: map
      robot_base_frame: base_footprint
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
      footprint: '[[0.120726, 0.0], [0.11783, 0.029405], [0.109252, 0.05768], [0.095324,
        0.083739], [0.076579, 0.106579], [0.053739, 0.125324], [0.02768, 0.139252],
        [-0.000595, 0.14783], [-0.03, 0.150726], [-0.059405, 0.14783], [-0.08768,
        0.139252], [-0.113739, 0.125324], [-0.136579, 0.106579], [-0.155324, 0.083739],
        [-0.169252, 0.05768], [-0.17783, 0.029405], [-0.180726, 0.0], [-0.17783, -0.029405],
        [-0.169252, -0.05768], [-0.155324, -0.083739], [-0.136579, -0.106579], [-0.113739,
        -0.125324], [-0.08768, -0.139252], [-0.059405, -0.14783], [-0.03, -0.150726],
        [-0.000595, -0.14783], [0.02768, -0.139252], [0.053739, -0.125324], [0.076579,
        -0.106579], [0.095324, -0.083739], [0.109252, -0.05768], [0.11783, -0.029405]]'
      footprint_padding: 0.02
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


## src/vacuum_sim/config/vacuum_navigate.xml

<root BTCPP_format="4" main_tree_to_execute="MainTree">
  <BehaviorTree ID="MainTree">
    <RecoveryNode number_of_retries="2" name="BoundedWaitAndReplan">
      <PipelineSequence name="NavigateWithReplanning">
        <RateController hz="1.0">
          <ComputePathToPose goal="{goal}" path="{path}" planner_id="GridBased" error_code_id="{compute_path_error_code}"/>
        </RateController>
        <FollowPath path="{path}" controller_id="FollowPath" error_code_id="{follow_path_error_code}"/>
      </PipelineSequence>
      <Wait wait_duration="3.0"/>
    </RecoveryNode>
  </BehaviorTree>
</root>


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


## src/vacuum_sim/config/drive.rviz

Panels:
- Class: rviz_common/Displays
  Help Height: 70
  Name: Displays
  Property Tree Widget:
    Expanded: null
    Splitter Ratio: 0.5
  Tree Height: 208
- Class: rviz_common/Tool Properties
  Expanded: null
  Name: Tool Properties
  Splitter Ratio: 0.5
Visualization Manager:
  Class: ''
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
    Description File: ''
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
    TF Prefix: ''
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
    Frame Rate: 60
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
    Saved: null
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


## src/vacuum_sim/config/vacuum_nav2.yaml

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
    navigate_to_pose:
      plugin: nav2_bt_navigator::NavigateToPoseNavigator
    navigate_through_poses:
      plugin: nav2_bt_navigator::NavigateThroughPosesNavigator
    error_code_names:
    - compute_path_error_code
    - follow_path_error_code
    use_sim_time: true
    enable_stamped_cmd_vel: false
    default_nav_to_pose_bt_xml: /home/robot/vacuum_ws/src/vacuum_sim/config/vacuum_navigate.xml
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
      xy_goal_tolerance: 0.1
      yaw_goal_tolerance: 0.2
    FollowPath:
      plugin: dwb_core::DWBLocalPlanner
      debug_trajectory_details: false
      min_vel_x: 0.0
      max_vel_x: 0.2
      min_vel_y: 0.0
      max_vel_y: 0.0
      max_vel_theta: 0.7
      min_speed_xy: 0.0
      max_speed_xy: 0.2
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
      xy_goal_tolerance: 0.1
      trans_stopped_velocity: 0.02
      short_circuit_trajectory_evaluation: true
      stateful: true
      critics:
      - RotateToGoal
      - Oscillation
      - ObstacleFootprint
      - GoalAlign
      - PathAlign
      - PathDist
      - GoalDist
      PathAlign.scale: 32.0
      PathAlign.forward_point_distance: 0.1
      GoalAlign.scale: 24.0
      GoalAlign.forward_point_distance: 0.1
      PathDist.scale: 32.0
      GoalDist.scale: 24.0
      RotateToGoal.scale: 32.0
      RotateToGoal.slowing_factor: 5.0
      RotateToGoal.lookahead_time: -1.0
      ObstacleFootprint.scale: 1.0
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
      plugins:
      - obstacle_layer
      - inflation_layer
      inflation_layer:
        plugin: nav2_costmap_2d::InflationLayer
        cost_scaling_factor: 4.0
        inflation_radius: 0.5
      static_layer:
        plugin: nav2_costmap_2d::StaticLayer
        map_subscribe_transient_local: true
      always_send_full_costmap: true
      use_sim_time: true
      footprint: '[[0.120726, 0.0], [0.11783, 0.029405], [0.109252, 0.05768], [0.095324,
        0.083739], [0.076579, 0.106579], [0.053739, 0.125324], [0.02768, 0.139252],
        [-0.000595, 0.14783], [-0.03, 0.150726], [-0.059405, 0.14783], [-0.08768,
        0.139252], [-0.113739, 0.125324], [-0.136579, 0.106579], [-0.155324, 0.083739],
        [-0.169252, 0.05768], [-0.17783, 0.029405], [-0.180726, 0.0], [-0.17783, -0.029405],
        [-0.169252, -0.05768], [-0.155324, -0.083739], [-0.136579, -0.106579], [-0.113739,
        -0.125324], [-0.08768, -0.139252], [-0.059405, -0.14783], [-0.03, -0.150726],
        [-0.000595, -0.14783], [0.02768, -0.139252], [0.053739, -0.125324], [0.076579,
        -0.106579], [0.095324, -0.083739], [0.109252, -0.05768], [0.11783, -0.029405]]'
      footprint_padding: 0.02
      obstacle_layer:
        plugin: nav2_costmap_2d::ObstacleLayer
        enabled: true
        max_obstacle_height: 2.0
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
global_costmap:
  global_costmap:
    ros__parameters:
      update_frequency: 1.0
      publish_frequency: 1.0
      global_frame: map
      robot_base_frame: base_footprint
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
        cost_scaling_factor: 4.0
        inflation_radius: 0.5
      always_send_full_costmap: true
      use_sim_time: true
      footprint: '[[0.120726, 0.0], [0.11783, 0.029405], [0.109252, 0.05768], [0.095324,
        0.083739], [0.076579, 0.106579], [0.053739, 0.125324], [0.02768, 0.139252],
        [-0.000595, 0.14783], [-0.03, 0.150726], [-0.059405, 0.14783], [-0.08768,
        0.139252], [-0.113739, 0.125324], [-0.136579, 0.106579], [-0.155324, 0.083739],
        [-0.169252, 0.05768], [-0.17783, 0.029405], [-0.180726, 0.0], [-0.17783, -0.029405],
        [-0.169252, -0.05768], [-0.155324, -0.083739], [-0.136579, -0.106579], [-0.113739,
        -0.125324], [-0.08768, -0.139252], [-0.059405, -0.14783], [-0.03, -0.150726],
        [-0.000595, -0.14783], [0.02768, -0.139252], [0.053739, -0.125324], [0.076579,
        -0.106579], [0.095324, -0.083739], [0.109252, -0.05768], [0.11783, -0.029405]]'
      footprint_padding: 0.02
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
      tolerance: 0.1
      use_astar: true
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
    - 0.2
    - 0.0
    - 0.7
    min_velocity:
    - 0.0
    - 0.0
    - -0.7
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
    cmd_vel_in_topic: /vacuum/selected_cmd_vel
    cmd_vel_out_topic: cmd_vel
    state_topic: collision_monitor_state
    transform_tolerance: 0.2
    source_timeout: 0.5
    base_shift_correction: true
    stop_pub_timeout: 2.0
    polygons:
    - StopZone
    - SlowZone
    - FootprintApproach
    FootprintApproach:
      type: polygon
      action_type: approach
      footprint_topic: /local_costmap/published_footprint
      time_before_collision: 1.2
      simulation_time_step: 0.04
      min_points: 1
      visualize: false
      enabled: true
    observation_sources:
    - scan
    scan:
      type: scan
      topic: scan
      min_height: 0.0
      max_height: 2.0
      enabled: true
      source_timeout: 0.5
    use_sim_time: true
    enable_stamped_cmd_vel: false
    StopZone:
      type: velocity_polygon
      action_type: stop
      min_points: 1
      visualize: true
      polygon_pub_topic: vacuum_stopzone
      enabled: true
      holonomic: false
      velocity_polygons:
      - forward
      - reverse
      - rotation
      forward:
        points: '[[-0.03, 0.19], [-0.03, -0.19], [0.42, -0.19], [0.42, 0.19]]'
        linear_min: 0.001
        linear_max: 1.0
        theta_min: -2.0
        theta_max: 2.0
      reverse:
        points: '[[-0.46, 0.19], [-0.46, -0.19], [-0.03, -0.19], [-0.03, 0.19]]'
        linear_min: -1.0
        linear_max: -0.001
        theta_min: -2.0
        theta_max: 2.0
      rotation:
        points: '[[0.170968, 0.0], [0.167106, 0.039207], [0.15567, 0.076907], [0.137099,
          0.111652], [0.112106, 0.142106], [0.081652, 0.167099], [0.046907, 0.18567],
          [0.009207, 0.197106], [-0.03, 0.200968], [-0.069207, 0.197106], [-0.106907,
          0.18567], [-0.141652, 0.167099], [-0.172106, 0.142106], [-0.197099, 0.111652],
          [-0.21567, 0.076907], [-0.227106, 0.039207], [-0.230968, 0.0], [-0.227106,
          -0.039207], [-0.21567, -0.076907], [-0.197099, -0.111652], [-0.172106, -0.142106],
          [-0.141652, -0.167099], [-0.106907, -0.18567], [-0.069207, -0.197106], [-0.03,
          -0.200968], [0.009207, -0.197106], [0.046907, -0.18567], [0.081652, -0.167099],
          [0.112106, -0.142106], [0.137099, -0.111652], [0.15567, -0.076907], [0.167106,
          -0.039207]]'
        linear_min: -1.0
        linear_max: 1.0
        theta_min: -2.0
        theta_max: 2.0
    SlowZone:
      type: velocity_polygon
      action_type: slowdown
      min_points: 1
      visualize: true
      polygon_pub_topic: vacuum_slowzone
      enabled: true
      holonomic: false
      velocity_polygons:
      - forward
      - reverse
      - rotation
      slowdown_ratio: 0.4
      forward:
        points: '[[-0.03, 0.24], [-0.03, -0.24], [0.9, -0.24], [0.9, 0.24]]'
        linear_min: 0.001
        linear_max: 1.0
        theta_min: -2.0
        theta_max: 2.0
      reverse:
        points: '[[-0.8, 0.24], [-0.8, -0.24], [-0.03, -0.24], [-0.03, 0.24]]'
        linear_min: -1.0
        linear_max: -0.001
        theta_min: -2.0
        theta_max: 2.0
      rotation:
        points: '[[0.251355, 0.0], [0.245949, 0.05489], [0.229938, 0.10767], [0.203938,
          0.156312], [0.168948, 0.198948], [0.126312, 0.233938], [0.07767, 0.259938],
          [0.02489, 0.275949], [-0.03, 0.281355], [-0.08489, 0.275949], [-0.13767,
          0.259938], [-0.186312, 0.233938], [-0.228948, 0.198948], [-0.263938, 0.156312],
          [-0.289938, 0.10767], [-0.305949, 0.05489], [-0.311355, 0.0], [-0.305949,
          -0.05489], [-0.289938, -0.10767], [-0.263938, -0.156312], [-0.228948, -0.198948],
          [-0.186312, -0.233938], [-0.13767, -0.259938], [-0.08489, -0.275949], [-0.03,
          -0.281355], [0.02489, -0.275949], [0.07767, -0.259938], [0.126312, -0.233938],
          [0.168948, -0.198948], [0.203938, -0.156312], [0.229938, -0.10767], [0.245949,
          -0.05489]]'
        linear_min: -1.0
        linear_max: 1.0
        theta_min: -2.0
        theta_max: 2.0
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


## src/vacuum_sim/config/controllers.yaml

controller_manager:
  ros__parameters:
    update_rate: 60
    use_sim_time: true
    joint_state_broadcaster:
      type: joint_state_broadcaster/JointStateBroadcaster
    diff_drive_controller:
      type: diff_drive_controller/DiffDriveController
diff_drive_controller:
  ros__parameters:
    use_sim_time: true
    left_wheel_names:
    - left_wheel_joint
    right_wheel_names:
    - right_wheel_joint
    wheel_separation: 0.22
    wheel_radius: 0.05
    publish_rate: 30.0
    odom_frame_id: odom
    base_frame_id: base_footprint
    enable_odom_tf: true
    open_loop: false
    position_feedback: true
    cmd_vel_timeout: 0.5
    pose_covariance_diagonal:
    - 0.001
    - 0.001
    - 0.001
    - 0.001
    - 0.001
    - 0.01
    twist_covariance_diagonal:
    - 0.001
    - 0.001
    - 0.001
    - 0.001
    - 0.001
    - 0.01
    linear.x.has_velocity_limits: true
    linear.x.max_velocity: 0.5
    linear.x.min_velocity: -0.3
    linear.x.has_acceleration_limits: true
    linear.x.max_acceleration: 0.8
    linear.x.min_acceleration: -0.8
    angular.z.has_velocity_limits: true
    angular.z.max_velocity: 1.2
    angular.z.min_velocity: -1.2
    angular.z.has_acceleration_limits: true
    angular.z.max_acceleration: 2.0
    angular.z.min_acceleration: -2.0


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

"""Local destination navigation, with only the servers used by this robot's BT."""
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    params = LaunchConfiguration('params_file')
    servers = [
        ('nav2_controller', 'controller_server', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_planner', 'planner_server', []),
        ('nav2_behaviors', 'behavior_server', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_velocity_smoother', 'velocity_smoother', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_collision_monitor', 'collision_monitor', []),
        ('nav2_bt_navigator', 'bt_navigator', []),
    ]
    actions = [DeclareLaunchArgument('params_file', default_value=str(package / 'config/vacuum_nav2.yaml'))]
    for pkg, name, remap in servers:
        actions.append(Node(package=pkg, executable=name, name=name,
                            parameters=[params, {'use_sim_time': True}],
                            remappings=[('/tf','tf'),('/tf_static','tf_static')] + remap,
                            output='screen'))
    # Allow process/plugin startup and local discovery before lifecycle requests.
    # All commands still pass through the gate and Collision Monitor.
    actions.append(TimerAction(period=4., actions=[Node(
        package='nav2_lifecycle_manager', executable='lifecycle_manager',
        name='lifecycle_manager_navigation', output='screen',
        parameters=[{'use_sim_time': True, 'autostart': True,
                     'node_names': [name for _, name, _ in servers],
                     'bond_timeout': 4.0}])]))
    return LaunchDescription(actions)


## src/vacuum_sim/launch/navigation.launch.py.before-autonomy-20261006

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
        DeclareLaunchArgument('camera_rate', default_value='60'),
        DeclareLaunchArgument('gui', default_value='true'),
        DeclareLaunchArgument('rviz', default_value='true'),
        DeclareLaunchArgument('rviz_config', default_value=str(package / 'config/view.rviz')),
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
        Node(package='rviz2', executable='rviz2', arguments=['-d', LaunchConfiguration('rviz_config')],
             parameters=[{'use_sim_time': True}], condition=IfCondition(LaunchConfiguration('rviz')), output='screen'),
    ])


## src/vacuum_sim/worlds

## src/vacuum_sim/worlds/room.sdf

<sdf version="1.9">
  <world name="vacuum_room">
    <physics name="physics" type="ignored">
      <max_step_size>0.005555555555555556</max_step_size>
      <real_time_factor>1.0</real_time_factor>
    </physics>
    <gravity>0 0 -9.81</gravity>
    <plugin filename="gz-sim-physics-system" name="gz::sim::systems::Physics" />
    <plugin filename="gz-sim-user-commands-system" name="gz::sim::systems::UserCommands" />
    <plugin filename="gz-sim-scene-broadcaster-system" name="gz::sim::systems::SceneBroadcaster" />
    <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors">
      <render_engine>ogre2</render_engine>
    </plugin>
    <scene>
      <ambient>.7 .7 .7 1</ambient>
      <background>.69 .79 .85 1</background>
      <shadows>false</shadows>
    </scene>
    <light name="afternoon_daylight" type="directional">
      <pose>0 0 6 0 0 0</pose>
      <diffuse>.75 .72 .65 1</diffuse>
      <specular>.15 .15 .15 1</specular>
      <direction>-.5 -.4 -1</direction>
      <cast_shadows>false</cast_shadows>
    </light>
    <light name="soft_window_fill" type="directional">
      <pose>0 0 6 0 0 0</pose>
      <diffuse>.25 .28 .3 1</diffuse>
      <specular>0 0 0 1</specular>
      <direction>.4 .4 -1</direction>
      <cast_shadows>false</cast_shadows>
    </light>
    <gui fullscreen="false">
      <camera name="user_camera">
        <pose>7 -9 8 0 .60 2.2</pose>
      </camera>
    </gui>
    <model name="furnished_living_room">
      <static>true</static>
      <self_collide>false</self_collide>
      <link name="room">
        <collision name="architecture_proxy0">
          <pose>0.0 0.0 -0.04 0 0 0</pose>
          <geometry>
            <box>
              <size>8.2 7.2 0.08</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy1">
          <pose>0.0 -3.5 1.4 0 0 0</pose>
          <geometry>
            <box>
              <size>8.2 0.12 2.8</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy2">
          <pose>-4.0 0.0 1.4 0 0 0</pose>
          <geometry>
            <box>
              <size>0.12 7 2.8</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy3">
          <pose>4.0 0.0 1.4 0 0 0</pose>
          <geometry>
            <box>
              <size>0.12 7 2.8</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy4">
          <pose>0.0 3.5 0.45 0 0 0</pose>
          <geometry>
            <box>
              <size>8.2 0.12 0.9</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy5">
          <pose>0.0 3.5 2.65 0 0 0</pose>
          <geometry>
            <box>
              <size>8.2 0.12 0.3</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy6">
          <pose>-3.15 3.5 1.7 0 0 0</pose>
          <geometry>
            <box>
              <size>1.9 0.12 1.6</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy7">
          <pose>3.15 3.5 1.7 0 0 0</pose>
          <geometry>
            <box>
              <size>1.9 0.12 1.6</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy0">
          <pose>-0.65 2.72 0.28 0 0 0</pose>
          <geometry>
            <box>
              <size>2.55 0.9 0.3</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy1">
          <pose>-0.65 3.08 0.65 0 0 0</pose>
          <geometry>
            <box>
              <size>2.55 0.21 0.75</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy2">
          <pose>-1.8599999999999999 2.6900000000000004 0.53 0 0 0</pose>
          <geometry>
            <box>
              <size>0.18 0.87 0.56</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy3">
          <pose>0.5599999999999999 2.6900000000000004 0.53 0 0 0</pose>
          <geometry>
            <box>
              <size>0.18 0.87 0.56</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy4">
          <pose>-1.73 2.4200000000000004 0.09 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.18</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy5">
          <pose>0.43000000000000005 2.4200000000000004 0.09 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.18</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy6">
          <pose>-1.73 3.02 0.09 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.18</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy7">
          <pose>0.43000000000000005 3.02 0.09 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.18</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy0">
          <pose>-0.65 1.32 0.4 0 0 0</pose>
          <geometry>
            <box>
              <size>1.25 0.63 0.07</size>
            </box>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy1">
          <pose>-1.12 1.11 0.2 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.4</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy2">
          <pose>-1.12 1.53 0.2 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.4</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy3">
          <pose>-0.18000000000000005 1.11 0.2 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.4</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy4">
          <pose>-0.18000000000000005 1.53 0.2 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.4</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="oak_media_console_proxy0">
          <pose>3.65 0.7 0.35 0 0 0</pose>
          <geometry>
            <box>
              <size>0.45 2.05 0.51</size>
            </box>
          </geometry>
        </collision>
        <collision name="oak_media_console_proxy1">
          <pose>3.65 -0.12 0.075 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.15</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="oak_media_console_proxy2">
          <pose>3.65 1.52 0.075 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.15</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="bookcase_proxy0">
          <pose>-3.62 1.55 0.105 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.21</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy1">
          <pose>-3.75 1.55 1.05 0 0 0</pose>
          <geometry>
            <box>
              <size>0.12 1.2 2.1</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy2">
          <pose>-3.62 0.9800000000000001 1.05 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 0.045 2.1</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy3">
          <pose>-3.62 2.12 1.05 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 0.045 2.1</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy4">
          <pose>-3.62 1.55 0.06 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy5">
          <pose>-3.62 1.55 0.5 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy6">
          <pose>-3.62 1.55 0.96 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy7">
          <pose>-3.62 1.55 1.42 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy8">
          <pose>-3.62 1.55 1.88 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy9">
          <pose>-3.62 1.55 2.12 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_table_proxy0">
          <pose>-2.4 -1.55 0.76 0 0 0</pose>
          <geometry>
            <box>
              <size>1.45 0.88 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_table_proxy1">
          <pose>-2.98 -1.85 0.37 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.045</radius>
              <length>0.74</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_table_proxy2">
          <pose>-2.98 -1.25 0.37 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.045</radius>
              <length>0.74</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_table_proxy3">
          <pose>-1.8199999999999998 -1.85 0.37 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.045</radius>
              <length>0.74</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_table_proxy4">
          <pose>-1.8199999999999998 -1.25 0.37 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.045</radius>
              <length>0.74</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy0">
          <pose>-2.4 -0.78 0.45 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy1">
          <pose>-2.4 -0.9750000000000001 0.72 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy2">
          <pose>-2.2399999999999998 -0.6200000000000001 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy3">
          <pose>-2.2399999999999998 -0.9400000000000001 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy4">
          <pose>-2.56 -0.62 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy5">
          <pose>-2.56 -0.94 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy0">
          <pose>-2.4 -2.33 0.45 0 0 0</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy1">
          <pose>-2.4 -2.1350000000000002 0.72 0 0 0</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy2">
          <pose>-2.56 -2.49 0.225 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy3">
          <pose>-2.56 -2.17 0.225 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy4">
          <pose>-2.2399999999999998 -2.49 0.225 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy5">
          <pose>-2.2399999999999998 -2.17 0.225 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy0">
          <pose>-3.47 -1.55 0.45 0 0 -1.5707963267948966</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy1">
          <pose>-3.2750000000000004 -1.55 0.72 0 0 -1.5707963267948966</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy2">
          <pose>-3.6300000000000003 -1.3900000000000001 0.225 0 0 -1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy3">
          <pose>-3.31 -1.3900000000000001 0.225 0 0 -1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy4">
          <pose>-3.6300000000000003 -1.71 0.225 0 0 -1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy5">
          <pose>-3.31 -1.71 0.225 0 0 -1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy0">
          <pose>2.2 -2.95 0.76 0 0 0</pose>
          <geometry>
            <box>
              <size>1.65 0.65 0.055</size>
            </box>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy1">
          <pose>1.5000000000000002 -3.18 0.37 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.045 0.74</size>
            </box>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy2">
          <pose>1.5000000000000002 -2.72 0.37 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.045 0.74</size>
            </box>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy3">
          <pose>2.9000000000000004 -3.18 0.37 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.045 0.74</size>
            </box>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy4">
          <pose>2.9000000000000004 -2.72 0.37 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.045 0.74</size>
            </box>
          </geometry>
        </collision>
        <collision name="office_chair_proxy0">
          <pose>2.2 -2.1 0.45 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="office_chair_proxy1">
          <pose>2.2 -2.295 0.72 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="office_chair_proxy2">
          <pose>2.3600000000000003 -1.9400000000000002 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="office_chair_proxy3">
          <pose>2.3600000000000003 -2.2600000000000002 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="office_chair_proxy4">
          <pose>2.04 -1.94 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="office_chair_proxy5">
          <pose>2.04 -2.2600000000000002 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="floor_lamp_proxy0">
          <pose>1.3 2.72 0.105 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.2</radius>
              <length>0.21</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="floor_lamp_proxy1">
          <pose>1.3 2.72 0.77 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.018</radius>
              <length>1.5</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="window_plant_proxy0">
          <pose>2.9 2.82 0.18 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.22</radius>
              <length>0.36</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="entry_plant_proxy0">
          <pose>-3.45 -2.87 0.18 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.22</radius>
              <length>0.36</length>
            </cylinder>
          </geometry>
        </collision>
        <visual name="furnished_room">
          <geometry>
            <mesh>
              <uri>/home/robot/vacuum_ws/src/vacuum_sim/worlds/furnished/living_room.dae</uri>
            </mesh>
          </geometry>
          <cast_shadows>false</cast_shadows>
        </visual>
      </link>
    </model>
  </world>
</sdf>


## src/vacuum_sim/worlds/furnished

## src/vacuum_sim/worlds/furnished/linen.png

## src/vacuum_sim/worlds/furnished/window_plant.dae

## src/vacuum_sim/worlds/furnished/oak_media_console.dae

## src/vacuum_sim/worlds/furnished/woven-rug.png

## src/vacuum_sim/worlds/furnished/dining_table.dae

## src/vacuum_sim/worlds/furnished/dining_chair_north.dae

## src/vacuum_sim/worlds/furnished/architecture.dae

## src/vacuum_sim/worlds/furnished/bookcase.dae

## src/vacuum_sim/worlds/furnished/landscape.png

## src/vacuum_sim/worlds/furnished/dining_chair_west.dae

## src/vacuum_sim/worlds/furnished/rounded_coffee_table.dae

## src/vacuum_sim/worlds/furnished/framed_wall_art.dae

## src/vacuum_sim/worlds/furnished/garden.png

## src/vacuum_sim/worlds/furnished/three_seat_sofa.dae

## src/vacuum_sim/worlds/furnished/entry_plant.dae

## src/vacuum_sim/worlds/furnished/oak.png

## src/vacuum_sim/worlds/furnished/floor_lamp.dae

## src/vacuum_sim/worlds/furnished/office_chair.dae

## src/vacuum_sim/worlds/furnished/woven_living_room_rug.dae

## src/vacuum_sim/worlds/furnished/living_room.dae

## src/vacuum_sim/worlds/furnished/dining_chair_south.dae

## src/vacuum_sim/worlds/furnished/home_office_desk.dae

## src/vacuum_sim/urdf

## src/vacuum_sim/urdf/vacuum.urdf.xacro

<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="vacuum">
  
  <xacro:arg name="controllers_file" default="$(find vacuum_sim)/config/controllers.yaml" />
  <xacro:arg name="camera_width" default="320" />
  <xacro:arg name="camera_height" default="240" />
  <xacro:arg name="camera_rate" default="60" />
  <xacro:property name="wheel_radius" value="0.05" />
  <xacro:property name="wheel_separation" value="0.22" />
  <xacro:property name="wheel_width" value="0.025" />
  <xacro:property name="body_x" value="0.30" />
  <xacro:property name="body_y" value="0.25" />
  <xacro:property name="body_z" value="0.10" />
  <xacro:property name="body_mass" value="3.0" />
  <material name="acrylic"><color rgba="0.2 0.65 0.85 0.6" /></material>
  <material name="rubber"><color rgba="0.08 0.08 0.10 1" /></material>
  <material name="sensor"><color rgba="0.15 0.18 0.20 1" /></material>

  <link name="base_footprint" />
  
  <joint name="base_joint" type="fixed"><parent link="base_footprint" /><child link="base_link" /><origin xyz="-0.03 0 0.08" /></joint>
  <link name="base_link">
    <inertial><mass value="${body_mass}" /><inertia ixx="${body_mass*(3*0.15**2+body_z**2)/12}" iyy="${body_mass*(3*0.15**2+body_z**2)/12}" izz="${body_mass*0.15**2/2}" ixy="0" ixz="0" iyz="0" /></inertial>
    <collision><geometry><cylinder radius="0.15" length="${body_z}" /></geometry></collision>
    <visual><origin xyz="0 0 -0.048" /><geometry><cylinder radius="0.15" length="0.004" /></geometry><material name="acrylic" /></visual>
    <visual><origin xyz="0 0 0.048" /><geometry><cylinder radius="0.15" length="0.004" /></geometry><material name="acrylic" /></visual>
    <visual><geometry><box size="0.20 0.16 0.065" /></geometry><material name="sensor" /></visual>
  </link>

  <xacro:macro name="wheel" params="side sign">
    <link name="${side}_wheel">
      <inertial><mass value="0.12" /><inertia ixx="${0.12*(3*wheel_radius**2+wheel_width**2)/12}" iyy="${0.12*wheel_radius**2/2}" izz="${0.12*(3*wheel_radius**2+wheel_width**2)/12}" ixy="0" ixz="0" iyz="0" /></inertial>
      <visual><origin rpy="${pi/2} 0 0" /><geometry><cylinder radius="${wheel_radius}" length="${wheel_width}" /></geometry><material name="rubber" /></visual>
      <collision><origin rpy="${pi/2} 0 0" /><geometry><cylinder radius="${wheel_radius}" length="${wheel_width}" /></geometry></collision>
    </link>
    <joint name="${side}_wheel_joint" type="continuous">
      <parent link="base_link" /><child link="${side}_wheel" />
      <origin xyz="0.03 ${sign*wheel_separation/2} ${wheel_radius-0.08}" /><axis xyz="0 1 0" />
      <limit effort="3.0" velocity="10.0" /><dynamics damping="0.01" friction="0.0" />
    </joint>
    <gazebo reference="${side}_wheel"><mu1>1.0</mu1><mu2>1.0</mu2></gazebo>
  </xacro:macro>
  <xacro:wheel side="left" sign="1" /><xacro:wheel side="right" sign="-1" />

  
  <joint name="caster_joint" type="fixed"><parent link="base_link" /><child link="caster" /><origin xyz="-0.105 0 -0.06" /></joint>
  <link name="caster">
    <inertial><mass value="0.08" /><inertia ixx="0.0000128" iyy="0.0000128" izz="0.0000128" ixy="0" ixz="0" iyz="0" /></inertial>
    <visual><geometry><sphere radius="0.02" /></geometry><material name="rubber" /></visual>
    <collision><geometry><sphere radius="0.02" /></geometry></collision>
  </link>
  <gazebo reference="caster_joint"><preserveFixedJoint>true</preserveFixedJoint></gazebo>
  <gazebo reference="caster"><mu1>0.01</mu1><mu2>0.01</mu2></gazebo>

  <joint name="lidar_joint" type="fixed"><parent link="base_link" /><child link="lidar_link" /><origin xyz="0 0 0.085" /></joint>
  <link name="lidar_link">
    <inertial><mass value="0.05" /><inertia ixx="0.00001" iyy="0.00001" izz="0.00002" ixy="0" ixz="0" iyz="0" /></inertial>
    <visual><geometry><cylinder radius="0.03" length="0.025" /></geometry><material name="sensor" /></visual>
    <collision><geometry><cylinder radius="0.03" length="0.025" /></geometry></collision>
  </link>
  <gazebo reference="lidar_joint"><preserveFixedJoint>true</preserveFixedJoint></gazebo>
  <gazebo reference="lidar_link">
    
    <sensor name="lidar" type="gpu_lidar">
      <topic>/scan</topic><gz_frame_id>lidar_link</gz_frame_id><update_rate>10</update_rate><always_on>true</always_on>
      <lidar><scan><horizontal><samples>360</samples><resolution>1</resolution><min_angle>${-pi}</min_angle><max_angle>${pi}</max_angle></horizontal></scan>
        <range><min>0.08</min><max>12.0</max><resolution>0.01</resolution></range>
        <noise><type>gaussian</type><mean>0</mean><stddev>0.005</stddev></noise>
      </lidar>
    </sensor>
  </gazebo>

  <joint name="camera_joint" type="fixed"><parent link="base_link" /><child link="camera_link" /><origin xyz="0.1325 0 0.025" /></joint>
  <link name="camera_link">
    <inertial><mass value="0.03" /><inertia ixx="0.000004" iyy="0.000004" izz="0.000004" ixy="0" ixz="0" iyz="0" /></inertial>
    <visual><geometry><box size="0.015 0.04 0.025" /></geometry><material name="sensor" /></visual>
  </link>
  <joint name="camera_optical_joint" type="fixed"><parent link="camera_link" /><child link="camera_optical_frame" /><origin rpy="${-pi/2} 0 ${-pi/2}" /></joint>
  <link name="camera_optical_frame" />
  <gazebo reference="camera_joint"><preserveFixedJoint>true</preserveFixedJoint></gazebo>
  <gazebo reference="camera_link">
    <sensor name="camera" type="camera"><topic>/camera/image_raw</topic><gz_frame_id>camera_optical_frame</gz_frame_id>
      <update_rate>$(arg camera_rate)</update_rate><always_on>true</always_on>
      <camera><horizontal_fov>1.0472</horizontal_fov><image><width>$(arg camera_width)</width><height>$(arg camera_height)</height><format>R8G8B8</format></image><clip><near>0.03</near><far>15</far></clip><camera_info_topic>/camera/camera_info</camera_info_topic></camera>
    </sensor>
  </gazebo>

  <ros2_control name="VacuumSimulation" type="system">
    <hardware><plugin>gz_ros2_control/GazeboSimSystem</plugin></hardware>
    <joint name="left_wheel_joint"><command_interface name="velocity" /><state_interface name="position" /><state_interface name="velocity" /></joint>
    <joint name="right_wheel_joint"><command_interface name="velocity" /><state_interface name="position" /><state_interface name="velocity" /></joint>
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
            outgoing.twist.linear.x = max(-0.30, min(0.50, message.linear.x))
            outgoing.twist.angular.z = max(-1.2, min(1.2, message.angular.z))
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

## tools/activate_guard.py

"""Activate the standalone simulator collision guard for direct driving."""
import os
import time
import rclpy
from rclpy.node import Node
from lifecycle_msgs.srv import GetState, ChangeState


def main():
    rclpy.init()
    node = Node(f'vacuum_guard_start_{os.getpid()}')
    get = node.create_client(GetState, '/collision_monitor/get_state')
    change = node.create_client(ChangeState, '/collision_monitor/change_state')

    def result(future):
        deadline = time.monotonic() + 15
        while not future.done() and time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=.05)
        if not future.done():
            raise RuntimeError('Collision guard lifecycle request timed out.')
        return future.result()

    try:
        if not get.wait_for_service(timeout_sec=20) or not change.wait_for_service(timeout_sec=20):
            raise RuntimeError('Collision guard is not available.')
        state = result(get.call_async(GetState.Request())).current_state.id
        for expected, transition in ((1, 1), (2, 3)):
            if state == expected:
                request = ChangeState.Request()
                request.transition.id = transition
                if not result(change.call_async(request)).success:
                    raise RuntimeError('Collision guard could not be activated.')
                state = result(get.call_async(GetState.Request())).current_state.id
        if state != 3:
            raise RuntimeError(f'Collision guard is in state {state}, not active.')
        print('Collision guard active.', flush=True)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()


## tools/prepare_lab.py

"""Apply the 30 cm chassis to the existing Ubuntu simulator, with rollback."""
from datetime import datetime
import math
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET
import yaml

WS = Path('/home/robot/vacuum_ws')
PACKAGE = WS / 'src/vacuum_sim'
XACRO = 'http://www.ros.org/wiki/xacro'
ET.register_namespace('xacro', XACRO)


def circle(radius, count=32):
    # Circumscribed polygon: never underestimate the circular shell.
    outer = radius / math.cos(math.pi / count)
    return [[round(-.03 + outer * math.cos(2 * math.pi * i / count), 6),
             round(outer * math.sin(2 * math.pi * i / count), 6)] for i in range(count)]


def prepare_driving_views():
    launch = PACKAGE / 'launch/sim.launch.py'
    text = launch.read_text()
    text = text.replace("DeclareLaunchArgument('camera_rate', default_value='5')",
                        "DeclareLaunchArgument('camera_rate', default_value='60')")
    if "DeclareLaunchArgument('rviz_config'" not in text:
        text = text.replace("DeclareLaunchArgument('rviz', default_value='true'),",
                            "DeclareLaunchArgument('rviz', default_value='true'),\n"
                            "        DeclareLaunchArgument('rviz_config', default_value=str(package / 'config/view.rviz')),")
        text = text.replace("arguments=['-d', str(package / 'config/view.rviz')]",
                            "arguments=['-d', LaunchConfiguration('rviz_config')]")
    compile(text, str(launch), 'exec')
    model = PACKAGE / 'urdf/vacuum.urdf.xacro'
    root = ET.fromstring(model.read_text())
    rate = root.find(f'{{{XACRO}}}arg[@name="camera_rate"]')
    if rate is None:
        raise RuntimeError('The camera rate argument is missing.')
    rate.set('default', '60')
    view = PACKAGE / 'config/view.rviz'
    data = yaml.safe_load(view.read_text())
    data['Visualization Manager']['Global Options']['Frame Rate'] = 60
    drive_data = yaml.safe_load(yaml.safe_dump(data))
    drive_data['Visualization Manager']['Global Options']['Fixed Frame'] = 'odom'
    drive_data['Visualization Manager']['Displays'] = [item for item in drive_data['Visualization Manager']['Displays']
                                                       if item.get('Class') != 'rviz_default_plugins/Map']
    updates = {launch: text, model: ET.tostring(root, encoding='unicode') + '\n',
               view: yaml.safe_dump(data, sort_keys=False),
               PACKAGE / 'config/drive.rviz': yaml.safe_dump(drive_data, sort_keys=False)}
    world = PACKAGE / 'worlds/room.sdf'
    scene = ET.fromstring(world.read_text())
    # 180 Hz physics divides into 60 Hz camera/control, 30 Hz odometry, 10 Hz lidar.
    # At the 0.5 m/s limit a physics step covers less than 3 mm.
    scene.find('world/physics/max_step_size').text = '0.005555555555555556'
    updates[world] = ET.tostring(scene, encoding='unicode') + '\n'
    changed = {path: value for path, value in updates.items() if not path.exists() or path.read_text() != value}
    if not changed:
        return
    backup = WS / 'model-backups' / datetime.now().strftime('camera60-%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True)
    originals = {path: path.read_bytes() if path.exists() else None for path in changed}
    for path, content in originals.items():
        if content is not None:
            saved = backup / path.relative_to(PACKAGE)
            saved.parent.mkdir(parents=True, exist_ok=True)
            saved.write_bytes(content)
    try:
        for path, value in changed.items():
            path.write_text(value)
        built = subprocess.run(['/bin/bash', '-lc',
                                'source env.sh; colcon build --symlink-install --packages-select vacuum_sim'],
                               cwd=WS, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
        if built.returncode:
            raise RuntimeError('Camera configuration build failed: ' + built.stdout[-4000:])
    except BaseException:
        for path, content in originals.items():
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(content)
        raise
    print('Camera target set to 60 FPS; direct driving view prepared.', flush=True)


def prepare():
    model = PACKAGE / 'urdf/vacuum.urdf.xacro'
    marker = WS / '.lab/circular-model-v1'
    prepare_driving_views()
    if marker.exists():
        return
    root = ET.fromstring(model.read_text())
    props = {p.get('name'): p for p in root.findall(f'{{{XACRO}}}property')}
    for key in ('body_x', 'body_y', 'body_z', 'body_mass', 'wheel_separation'):
        if key not in props:
            raise RuntimeError(f'Unexpected robot model: missing {key}; no geometry changes applied.')
    props['wheel_separation'].set('value', '0.22')
    body = root.find("link[@name='base_link']")
    if body is None:
        raise RuntimeError('Expected chassis link was not found.')
    root.find("joint[@name='base_joint']/origin").set('xyz', '-0.03 0 0.08')
    inertia = body.find('inertial/inertia')
    inertia.set('ixx', '${body_mass*(3*0.15**2+body_z**2)/12}')
    inertia.set('iyy', '${body_mass*(3*0.15**2+body_z**2)/12}')
    inertia.set('izz', '${body_mass*0.15**2/2}')
    geom = body.find('collision/geometry')
    geom.clear()
    ET.SubElement(geom, 'cylinder', radius='0.15', length='${body_z}')
    plates = 0
    for visual in body.findall('visual'):
        geom = visual.find('geometry')
        box = geom.find('box')
        if box is not None and 'body_x' in box.get('size', ''):
            geom.clear()
            ET.SubElement(geom, 'cylinder', radius='0.15', length='0.004')
            plates += 1
        elif geom.find('cylinder') is not None:
            plate = geom.find('cylinder')
            if plate.get('radius') == '0.15' and plate.get('length') == '0.004':
                plates += 1
    if plates != 2:
        raise RuntimeError('Expected two acrylic plates; no geometry changes applied.')
    wheel = root.find(f'{{{XACRO}}}macro[@name="wheel"]/joint/origin')
    wheel.set('xyz', '0.03 ${sign*wheel_separation/2} ${wheel_radius-0.08}')
    root.find("joint[@name='caster_joint']/origin").set('xyz', '-0.105 0 -0.06')
    root.find("joint[@name='camera_joint']/origin").set('xyz', '0.1325 0 0.025')
    updates = {model: ET.tostring(root, encoding='unicode') + '\n'}
    controllers = PACKAGE / 'config/controllers.yaml'
    data = yaml.safe_load(controllers.read_text())
    data['diff_drive_controller']['ros__parameters']['wheel_separation'] = .22
    updates[controllers] = yaml.safe_dump(data, sort_keys=False)
    for name in ('nav2.yaml', 'vacuum_nav2.yaml'):
        path = PACKAGE / 'config' / name
        data = yaml.safe_load(path.read_text())
        for costmap in ('local_costmap', 'global_costmap'):
            params = data[costmap][costmap]['ros__parameters']
            params.pop('robot_radius', None)
            params['footprint'] = str(circle(.15))
            params['footprint_padding'] = .02
        params = data['collision_monitor']['ros__parameters']
        if name == 'vacuum_nav2.yaml':
            params['cmd_vel_in_topic'] = '/vacuum/selected_cmd_vel'
        for zone, radius in (('StopZone', .23), ('SlowZone', .35)):
            if zone in params:
                params[zone]['points'] = str(circle(radius))
        updates[path] = yaml.safe_dump(data, sort_keys=False)
    view = PACKAGE / 'config/view.rviz'
    data = yaml.safe_load(view.read_text())
    data['Visualization Manager']['Global Options']['Fixed Frame'] = 'map'
    updates[view] = yaml.safe_dump(data, sort_keys=False)
    backup = WS / 'model-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True)
    originals = {path: path.read_bytes() for path in updates}
    for path, content in originals.items():
        saved = backup / path.relative_to(PACKAGE)
        saved.parent.mkdir(parents=True, exist_ok=True)
        saved.write_bytes(content)
    try:
        for path, text in updates.items():
            path.write_text(text)
        built = subprocess.run(['/bin/bash', '-lc',
                                'source env.sh; colcon build --symlink-install --packages-select vacuum_sim'],
                               cwd=WS, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
        if built.returncode:
            raise RuntimeError('Model build failed: ' + built.stdout[-5000:])
        marker.parent.mkdir(exist_ok=True)
        marker.write_text('30 cm circular body; axle offset 3 cm; wheel separation 22 cm.\n'
                          f'Previous source files: {backup}\n'
                          'Previous navigation validation used the old body; rerun for this geometry.\n')
    except BaseException:
        for path, content in originals.items():
            path.write_bytes(content)
        raise
    print(f'30 cm circular chassis prepared. Previous source saved in {backup}', flush=True)


if __name__ == '__main__':
    prepare()


## tools/__pycache__

## tools/__pycache__/controller_bridge.cpython-312.pyc

## tools/__pycache__/command_gate.cpython-312.pyc

## tools/__pycache__/prepare_lab.cpython-312.pyc

## tools/validate_lab.py

"""Test an already-running launcher lab. Commands only the simulated robot."""
import json
import math
from pathlib import Path
import subprocess
import time
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from nav2_msgs.action import NavigateToPose

WS = Path('/home/robot/vacuum_ws')
report = {'date': '2026-10-07', 'scope': 'simulator only', 'tests': {}}
rclpy.init()
node = Node('vacuum_lab_validation', parameter_overrides=[rclpy.parameter.Parameter('use_sim_time', value=True)])
odom = []
commands = []
node.create_subscription(Odometry, '/odom', odom.append, qos_profile_sensor_data)
node.create_subscription(Twist, '/vacuum/selected_cmd_vel', commands.append, 10)
client = ActionClient(node, NavigateToPose, '/navigate_to_pose')
bridge = None


def wait(predicate, seconds):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        rclpy.spin_once(node, timeout_sec=.05)
        if predicate():
            return True
    return bool(predicate())


def run(action):
    result = subprocess.run(['python3', 'tools/lab_controller.py', action], cwd=WS,
                            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=100)
    print(result.stdout, flush=True)
    if result.returncode:
        raise RuntimeError(result.stdout)


try:
    assert wait(lambda: bool(odom) and bool(commands), 20), 'No odometry / command gate'
    assert client.wait_for_server(timeout_sec=10)
    goal = NavigateToPose.Goal()
    goal.pose.header.frame_id = 'map'
    goal.pose.header.stamp = node.get_clock().now().to_msg()
    goal.pose.pose.position.x = .6
    goal.pose.pose.orientation.w = 1.
    future = client.send_goal_async(goal)
    assert wait(future.done, 10)
    handle = future.result()
    assert handle.accepted, 'Navigation goal rejected'
    outcome = handle.get_result_async()
    if not wait(outcome.done, 100):
        cancellation = handle.cancel_goal_async()
        wait(cancellation.done, 5)
        raise RuntimeError('Navigation timed out; goal cancelled')
    result = outcome.result()
    assert result.status == 4 and result.result.error_code == 0, str(result)
    report['tests']['circular_robot_goal'] = {'status': result.status, 'error_code': result.result.error_code}
    print('Circular robot navigation goal passed.', flush=True)
    run('save-map')
    report['tests']['map_save'] = True
    run('manual')
    logfile = (WS / '.lab/bridge-validation.log').open('w')
    bridge = subprocess.Popen(['python3', 'tools/controller_bridge.py'], cwd=WS,
                              stdin=subprocess.PIPE, stdout=logfile, stderr=subprocess.STDOUT, text=True)

    def exercise(held, seconds):
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            assert bridge.poll() is None, 'Manual bridge exited'
            bridge.stdin.write(json.dumps({'v': .10, 'w': 0., 'held': held}) + '\n')
            bridge.stdin.flush()
            rclpy.spin_once(node, timeout_sec=.05)
            time.sleep(.02)

    # Allow DDS services and subscriptions to connect while sending zero input.
    exercise(False, 5)
    assert abs(odom[-1].twist.twist.linear.x) < .02, 'Robot moved while disarmed'
    start = odom[-1].pose.pose.position
    before = (start.x, start.y)
    exercise(True, 3)
    end = odom[-1].pose.pose.position
    movement = math.hypot(end.x-before[0], end.y-before[1])
    assert movement > .08, f'Manual drive did not move: {movement}'
    exercise(False, 2)
    assert abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02
    report['tests']['manual_hold_and_release'] = {'movement_m': movement, 'released_speed_m_s': odom[-1].twist.twist.linear.x}
    exercise(True, 1)
    # Keep the bridge alive, but stop supplying packets. Steady-time watchdog must stop.
    assert wait(lambda: abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02, 4)
    report['tests']['input_timeout_stop'] = True
    bridge.stdin.close()
    bridge.wait(timeout=5)
    assert bridge.returncode == 0
    report['tests']['bridge_eof_cleanup'] = True
    report['passed'] = True
except Exception as exc:
    report['passed'] = False
    report['error'] = str(exc)
    raise
finally:
    if bridge and bridge.poll() is None:
        try:
            bridge.stdin.close()
            bridge.wait(timeout=5)
        except Exception:
            bridge.terminate()
    target = WS / 'validation/lab-20261007'
    target.mkdir(parents=True, exist_ok=True)
    (target / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2), flush=True)
    node.destroy_node()
    rclpy.shutdown()


## tools/diagnose_manual.py

import json,subprocess,time,rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
rclpy.init(); node=Node('diagnose_manual'); latest={}
for topic in ['/vacuum/manual_cmd_vel','/vacuum/selected_cmd_vel','/cmd_vel']:
    node.create_subscription(Twist,topic,lambda m,t=topic: latest.update({t:m.linear.x}),10)
node.create_subscription(Odometry,'/odom',lambda m:latest.update({'odom':m.twist.twist.linear.x}),10)
p=subprocess.Popen(['python3','tools/controller_bridge.py'],stdin=subprocess.PIPE,text=True)
started=time.monotonic(); next_print=0
try:
    while time.monotonic()-started<9:
        elapsed=time.monotonic()-started
        p.stdin.write(json.dumps({'v':.1,'w':0.,'held':3<elapsed<7})+'\n');p.stdin.flush()
        rclpy.spin_once(node,timeout_sec=.05);time.sleep(.02)
        if elapsed>=next_print:
            print(round(elapsed,2),latest,flush=True);next_print=elapsed+1
finally:
    p.stdin.close();p.wait(timeout=5);node.destroy_node();rclpy.shutdown()


## tools/lab_controller.py

#!/usr/bin/env python3
"""User-owned, simulator-only launcher. No sudo, hardware, or global process killing."""
import argparse
import datetime
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import time
import yaml

WS = Path('/home/robot/vacuum_ws')
RUN = WS / '.lab'
STATE = RUN / 'processes.json'
SESSION = RUN / 'session.json'
CAMERA_RATE = 60


def say(message):
    print(message, flush=True)


def identity(pid):
    try:
        path = Path(f'/proc/{pid}')
        # comm may contain spaces, so split after its closing parenthesis.
        fields = (path / 'stat').read_text().rsplit(')', 1)[1].split()
        if fields[0] == 'Z' or path.stat().st_uid != os.getuid():
            return None
        return fields[19]  # /proc stat field 22: start time
    except (FileNotFoundError, ProcessLookupError, PermissionError):
        return None


def read_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save(state):
    tmp = STATE.with_suffix('.tmp')
    tmp.write_text(json.dumps(state))
    tmp.replace(STATE)


def alive(record):
    return identity(record['pid']) == record['start']


def member_alive(pid, stamp, group):
    try:
        return identity(int(pid)) == stamp and os.getpgid(int(pid)) == group and os.getsid(int(pid)) == group
    except ProcessLookupError:
        return False


def group_members(record):
    result = {}
    if not alive(record):
        return {pid: stamp for pid, stamp in record.get('members', {}).items()
                if member_alive(pid, stamp, record['pid'])}
    for path in Path('/proc').iterdir():
        if not path.name.isdigit():
            continue
        try:
            fields = (path / 'stat').read_text().rsplit(')', 1)[1].split()
            if int(fields[2]) == record['pid'] and int(fields[3]) == record['pid']:
                stamp = identity(int(path.name))
                if stamp is not None:
                    result[path.name] = stamp
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            pass
    return result


def stop(state):
    # Reverse startup order. Never signal a recycled PID or another user's process.
    for name, record in reversed(list(state.items())):
        members = group_members(record)
        if not members:
            continue
        record['members'] = members
        save(state)
        def still_running():
            return any(member_alive(pid, stamp, record['pid'])
                       for pid, stamp in members.items())
        say(f'Stopping {name}…')
        for sig, delay in ((signal.SIGTERM, 14), (signal.SIGKILL, 2)):
            if not still_running():
                break
            try:
                os.killpg(record['pid'], sig)
            except ProcessLookupError:
                break
            end = time.monotonic() + delay
            while still_running() and time.monotonic() < end:
                time.sleep(.2)
    remaining = {name: rec for name, rec in state.items() if group_members(rec)}
    save(remaining)
    (RUN / 'manual-mode').unlink(missing_ok=True)
    SESSION.unlink(missing_ok=True)
    if remaining:
        raise RuntimeError('Some lab processes did not stop. See .lab logs.')


def command(argv, timeout=20):
    return subprocess.run(['/bin/bash', '-lc', 'source env.sh; exec "$@"',
                           'vacuum-lab', *argv], cwd=WS, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=timeout)


def launch(state, name, argv):
    with (RUN / f'{name}.log').open('w') as log:
        proc = subprocess.Popen(['/bin/bash', '-lc', 'source env.sh; exec "$@"',
                                 'vacuum-lab', *argv], cwd=WS, stdin=subprocess.DEVNULL,
                                stdout=log, stderr=subprocess.STDOUT,
                                start_new_session=True)
    state[name] = {'pid': proc.pid, 'start': identity(proc.pid)}
    if state[name]['start'] is None:
        raise RuntimeError(f'{name} exited during startup. See .lab/{name}.log.')
    save(state)


def ready(state, target, seconds=60):
    result = command(['python3', 'tools/wait_ready.py', target, '--timeout', str(seconds)], seconds + 10)
    if any(not alive(rec) for rec in state.values()):
        raise RuntimeError('A lab component exited. See .lab logs.')
    if result.returncode or 'READY' not in result.stdout:
        raise RuntimeError(f'{target} startup timed out. See .lab logs. ' + result.stdout)


def start(state, gazebo):
    settings = json.loads(SESSION.read_text()) if SESSION.exists() else {}
    if set(state) == {'simulation', 'command gate', 'mapping', 'navigation'} and all(alive(rec) for rec in state.values()) and settings.get('camera_rate') == CAMERA_RATE and not (RUN / 'manual-mode').exists():
        say('Lab is already running. Stop and restart to leave manual mode or change the views.')
        return
    if state:
        stop(state)
        state.clear()
    required = [WS / 'env.sh', WS / 'tools/run_sim.py',
                WS / 'src/vacuum_sim/config/vacuum_nav2.yaml',
                WS / 'src/vacuum_sim/config/vacuum_navigate.xml']
    if any(not path.is_file() for path in required):
        raise RuntimeError('The simulator or conservative navigation profile is missing.')
    # Refuse to combine this session with an existing manually started ROS workload.
    nodes = command(['ros2', 'node', 'list']).stdout
    if any(name in nodes for name in ('/slam_toolbox', '/controller_server', '/robot_state_publisher')):
        raise RuntimeError('A manual lab session is running. Stop its terminals first.')
    from prepare_lab import prepare
    checked = command(['python3', 'tools/check_lab.py'], 30)
    if checked.returncode:
        raise RuntimeError('Controller safety logic checks failed: ' + checked.stdout)
    prepare()
    try:
        say('Starting simulator and RViz…')
        launch(state, 'simulation', ['python3', 'tools/run_sim.py',
                                    f'gui:={str(gazebo).lower()}', 'rviz:=true',
                                    f'camera_rate:={CAMERA_RATE}',
                                    'rviz_config:=' + str(WS / 'src/vacuum_sim/config/view.rviz')])
        ready(state, 'scan')
        launch(state, 'command gate', ['python3', 'tools/command_gate.py'])
        say('Starting mapping…')
        launch(state, 'mapping', ['ros2', 'launch', 'vacuum_sim', 'mapping.launch.py'])
        ready(state, 'map')
        say('Starting obstacle-aware navigation…')
        launch(state, 'navigation', ['ros2', 'launch', 'vacuum_sim', 'navigation.launch.py',
                                    'params_file:=' + str(required[2])])
        ready(state, 'navigation')
        SESSION.write_text(json.dumps({'mode': 'navigation', 'camera_rate': CAMERA_RATE}))
        say('Ready. In RViz set Fixed Frame to map, then use Nav2 Goal to choose a destination.')
        say('This is mapping and destination navigation. Automatic room cleaning is not implemented.')
    except BaseException:
        say('Startup failed; stopping this launcher’s processes…')
        stop(state)
        raise


def drive(state, gazebo):
    settings = json.loads(SESSION.read_text()) if SESSION.exists() else {}
    if set(state) == {'simulation', 'command gate', 'collision guard', 'camera view'} and all(alive(rec) for rec in state.values()) and settings.get('camera_rate') == CAMERA_RATE:
        ready(state, 'collision_monitor', 15)
        say('Ready to drive. Open the controller panel; push forward, pull back to reverse.')
        return
    if state:
        stop(state)
        state.clear()
    nodes = command(['ros2', 'node', 'list']).stdout
    if any(name in nodes for name in ('/slam_toolbox', '/controller_server', '/robot_state_publisher', '/collision_monitor')):
        raise RuntimeError('A manual lab session is running. Stop its terminals first.')
    from prepare_lab import prepare, circle
    prepare()
    checked = command(['python3', 'tools/check_lab.py'], 30)
    if checked.returncode:
        raise RuntimeError('Controller safety checks failed: ' + checked.stdout)
    config = yaml.safe_load((WS / 'src/vacuum_sim/config/vacuum_nav2.yaml').read_text())
    guard = config['collision_monitor']['ros__parameters']
    # Static approach footprint preserves predictive braking without a costmap.
    guard['FootprintApproach']['points'] = str(circle(.17))
    guard['cmd_vel_in_topic'] = '/vacuum/selected_cmd_vel'
    guard_path = RUN / 'drive-guard.yaml'
    guard_path.write_text(yaml.safe_dump({'collision_monitor': {'ros__parameters': guard}}, sort_keys=False))
    (RUN / 'manual-mode').write_text('Direct manual driving selected.\n')
    try:
        say('Starting 60 FPS camera and driving view…')
        launch(state, 'simulation', ['python3', 'tools/run_sim.py',
                                    f'gui:={str(gazebo).lower()}', 'rviz:=false',
                                    f'camera_rate:={CAMERA_RATE}',
                                    'rviz_config:=' + str(WS / 'src/vacuum_sim/config/drive.rviz')])
        ready(state, 'scan')
        launch(state, 'command gate', ['python3', 'tools/command_gate.py'])
        launch(state, 'collision guard', ['/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor',
                                         '--ros-args', '--params-file', str(guard_path)])
        activated = command(['python3', 'tools/activate_guard.py'], 65)
        if activated.returncode:
            raise RuntimeError(activated.stdout)
        launch(state, 'camera view', ['python3', '/opt/ros/jazzy/lib/rqt_image_view/rqt_image_view', '/camera/image_raw'])
        ready(state, 'collision_monitor', 15)
        SESSION.write_text(json.dumps({'mode': 'drive', 'camera_rate': CAMERA_RATE}))
        say('Ready to drive. Push forward, pull back to reverse. Camera target: 60 FPS.')
    except BaseException:
        say('Driving startup failed; stopping this launcher’s processes…')
        stop(state)
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['start', 'drive', 'stop', 'status', 'save-map', 'manual'])
    parser.add_argument('--gazebo', action='store_true')
    args = parser.parse_args()
    if not WS.is_dir():
        raise RuntimeError('Ubuntu vacuum workspace was not found.')
    RUN.mkdir(exist_ok=True)
    with (RUN / 'controller.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        state = read_state()
        if args.action == 'start':
            start(state, args.gazebo)
        elif args.action == 'drive':
            drive(state, args.gazebo)
        elif args.action == 'stop':
            stop(state)
            say('Lab stopped.')
        elif args.action == 'status':
            say('\n'.join(f'{name}: {"running" if alive(rec) else "stopped"}'
                          for name, rec in state.items()) or 'Lab is stopped.')
        elif args.action == 'manual':
            if set(state) == {'simulation', 'command gate', 'collision guard', 'camera view'} and all(alive(rec) for rec in state.values()):
                ready(state, 'collision_monitor', 15)
                say('Manual mode ready. Direct driving guard is active.')
                return
            if set(state) != {'simulation', 'command gate', 'mapping', 'navigation'} or any(not alive(rec) for rec in state.values()):
                raise RuntimeError('Start the lab before enabling manual drive.')
            # Switch the gate first: autonomous output cannot reach the robot,
            # even while cancellation is pending. Keep Nav2's managed nodes alive
            # so its bond manager does not tear down Collision Monitor.
            (RUN / 'manual-mode').write_text('Manual command source selected; restart to resume goals.\n')
            result = command(['ros2', 'service', 'call', '/navigate_to_pose/_action/cancel_goal',
                              'action_msgs/srv/CancelGoal', '{}'], 30)
            if result.returncode:
                raise RuntimeError('Could not cancel navigation; the gate remains stopped in manual mode. ' + result.stdout)
            ready(state, 'collision_monitor', 20)
            say('Manual mode ready. Navigation is paused until Stop lab → Start lab.')
        else:
            if not state.get('mapping') or not alive(state['mapping']):
                raise RuntimeError('Start the lab before saving a map.')
            maps = WS / 'maps'
            maps.mkdir(exist_ok=True)
            prefix = maps / datetime.datetime.now().strftime('room-%Y%m%d-%H%M%S-%f')
            result = command(['ros2', 'run', 'nav2_map_server', 'map_saver_cli',
                              '-f', str(prefix), '--ros-args', '-p', 'use_sim_time:=true',
                              '-p', 'save_map_timeout:=10.0',
                              '-p', 'map_subscribe_transient_local:=true'], 40)
            if result.returncode or not prefix.with_suffix('.yaml').is_file():
                raise RuntimeError('Map save failed: ' + result.stdout)
            say(f'Map saved: {prefix}.yaml\nSaved-map localization is a separate future workflow.')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        say(f'Error: {exc}')
        raise SystemExit(1)


## tools/controller_bridge.py

"""Manual simulator control via stdin; steady-time watchdog and Nav2 interlock."""
import json
import math
from pathlib import Path
import sys
import threading
import time
import rclpy
from geometry_msgs.msg import Twist
from lifecycle_msgs.srv import GetState
from nav2_msgs.msg import CollisionMonitorState
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from rclpy.qos import qos_profile_sensor_data
from rclpy.node import Node

MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')


def decode(line):
    data = json.loads(line)
    v, w = float(data['v']), float(data['w'])
    if not math.isfinite(v) or not math.isfinite(w):
        raise ValueError('Non-finite control input')
    if data.get('held') is not True:
        return 0., 0.
    return max(-.30, min(.50, v)), max(-1.2, min(1.2, w))


class Bridge(Node):
    def __init__(self):
        super().__init__('vacuum_manual_controller')
        self.pub = self.create_publisher(Twist, '/vacuum/manual_cmd_vel', 1)
        self.lock = threading.Lock()
        self.latest = (0., 0.)
        self.received = 0.
        self.closed = False
        self.states = {'collision_monitor': (0, 0.)}
        self.state_clients = {name: self.create_client(GetState, f'/{name}/get_state') for name in self.states}
        self.pending = {}
        self.last_status = None
        self.report_at = 0.
        self.guard_action = (0, '')
        self.output = (0., 0., 0.)
        self.scan_at = 0.
        self.odom = (0., 0., 0.)
        self.motion_since = 0.
        self.create_subscription(CollisionMonitorState, '/collision_monitor_state', self.guard_state, 10)
        self.create_subscription(Twist, '/cmd_vel', self.guard_output, 1)
        self.create_subscription(LaserScan, '/scan', self.scan_received, qos_profile_sensor_data)
        self.create_subscription(Odometry, '/odom', self.odom_received, qos_profile_sensor_data)
        self.create_timer(.05, self.tick)
        self.create_timer(.25, self.check_states)
        threading.Thread(target=self.read_input, daemon=True).start()

    def read_input(self):
        try:
            for line in sys.stdin:
                try:
                    command = decode(line)
                except (ValueError, KeyError, TypeError):
                    command = (0., 0.)
                with self.lock:
                    self.latest = command
                    self.received = time.monotonic()
        finally:
            with self.lock:
                self.latest = (0., 0.)
                self.closed = True

    def check_states(self):
        now = time.monotonic()
        for name, client in self.state_clients.items():
            previous = self.pending.get(name)
            if previous and not previous[0].done():
                if now - previous[1] < .75:
                    continue
                # A lost service response must not leave a permanently pending
                # future that prevents all subsequent health checks.
                self.pending.pop(name)
                client.remove_pending_request(previous[0])
                previous[0].cancel()
            if not client.service_is_ready():
                continue
            future = client.call_async(GetState.Request())
            self.pending[name] = (future, now)
            future.add_done_callback(lambda result, name=name: self.record(name, result))

    def record(self, name, future):
        if self.pending.get(name, (None,))[0] is not future:
            return
        try:
            self.states[name] = (future.result().current_state.id, time.monotonic())
        except Exception:
            self.states[name] = (0, 0.)

    def guard_state(self, message):
        self.guard_action = (message.action_type, message.polygon_name)

    def guard_output(self, message):
        self.output = (message.linear.x, message.angular.z, time.monotonic())

    def scan_received(self, message):
        self.scan_at = time.monotonic()

    def odom_received(self, message):
        self.odom = (message.twist.twist.linear.x, message.twist.twist.angular.z, time.monotonic())

    def report(self, now, safe, v, w):
        if now < self.report_at:
            return
        self.report_at = now + .25
        out_v, out_w, stamp = self.output
        actual_v, actual_w, odom_stamp = self.odom
        action, polygon = self.guard_action
        reason = 'Ready'
        if not MODE.exists():
            reason = 'Manual mode is not selected'
        elif now - self.scan_at > .5:
            reason = 'Lidar data missing or stale; guard stops motion'
        elif not safe:
            reason = 'Waiting for collision guard health; commands stopped'
        elif abs(v) + abs(w) > .001:
            if now - stamp > .5:
                reason = 'No fresh guard output; commands stopped'
            elif abs(out_v) + abs(out_w) < .001:
                if action and polygon:
                    escape = 'try reverse' if v > .001 else ('try forward' if v < -.001 else 'move away before turning')
                    reason = 'Obstacle blocks this direction; ' + escape
                else:
                    reason = 'Guard stopped motion; check lidar/TF in Ubuntu logs'
            elif abs(out_v) < abs(v) - .01 or abs(out_w) < abs(w) - .01:
                reason = 'Slowing near an obstacle'
            else:
                reason = 'Driving'
                if now - odom_stamp > 1.:
                    reason = 'Odometry missing; check simulator/controller'
                elif self.motion_since and now - self.motion_since > 1.5 and abs(actual_v) < .015 and abs(actual_w) < .04:
                    reason = 'No actual movement; STOP and check simulator/controller'
        print(json.dumps({'ready': safe, 'reason': reason, 'polygon': polygon,
                          'requested_v': v, 'output_v': out_v, 'output_w': out_w,
                          'actual_v': actual_v, 'actual_w': actual_w}), flush=True)

    def tick(self):
        now = time.monotonic()
        safe = MODE.exists() and now - self.scan_at < .5 and all(state == 3 and now - stamp < 1.
                                     for state, stamp in self.states.values())
        with self.lock:
            v, w = self.latest if safe and now - self.received < .3 else (0., 0.)
            closed = self.closed
        message = Twist()
        message.linear.x, message.angular.z = v, w
        if abs(v) + abs(w) > .03:
            if not self.motion_since:
                self.motion_since = now
        else:
            self.motion_since = 0.
        self.pub.publish(message)
        self.report(now, safe, v, w)
        if closed:
            raise KeyboardInterrupt


def main():
    # The launcher lock, separate from the simulator lock, serializes manual sources.
    import fcntl
    path = Path('/home/robot/vacuum_ws/.lab/manual-input.lock')
    with path.open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        rclpy.init()
        node = Bridge()
        try:
            rclpy.spin(node)
        except KeyboardInterrupt:
            pass
        finally:
            node.pub.publish(Twist())
            node.destroy_node()
            if rclpy.ok():
                rclpy.shutdown()


if __name__ == '__main__':
    main()


## tools/wait_ready.py

"""Wait for live ROS messages/services, without the ros2 CLI graph cache."""
import argparse
import os
import time
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy, qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from lifecycle_msgs.srv import GetState


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', choices=['scan', 'map', 'navigation', 'collision_monitor'])
    parser.add_argument('--timeout', type=float, default=60)
    args = parser.parse_args()
    rclpy.init()
    node = Node(f'vacuum_lab_readiness_{os.getpid()}')
    received = []
    clients = {}
    pending = {}
    active = set()
    if args.target == 'scan':
        node.create_subscription(LaserScan, '/scan', received.append, qos_profile_sensor_data)
    elif args.target == 'map':
        node.create_subscription(OccupancyGrid, '/map', received.append,
                                 QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL,
                                            reliability=ReliabilityPolicy.RELIABLE))
    else:
        names = ['controller_server', 'planner_server', 'collision_monitor', 'bt_navigator'] if args.target == 'navigation' else ['collision_monitor']
        clients = {name: node.create_client(GetState, f'/{name}/get_state') for name in names}
    deadline = time.monotonic() + args.timeout
    next_call = 0.
    try:
        while time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=.05)
            if received or (clients and len(active) == len(clients)):
                print('READY', flush=True)
                return 0
            if time.monotonic() >= next_call:
                for name, client in clients.items():
                    request = pending.get(name)
                    future = request[0] if request else None
                    if future and not future.done():
                        if time.monotonic() - request[1] < 2.:
                            continue
                        client.remove_pending_request(future)
                        future.cancel()
                        pending.pop(name)
                        active.discard(name)
                        future = None
                    if future:
                        try:
                            if future.result().current_state.id == 3:
                                active.add(name)
                            else:
                                active.discard(name)
                        except Exception:
                            active.discard(name)
                    if client.service_is_ready():
                        pending[name] = (client.call_async(GetState.Request()), time.monotonic())
                next_call = time.monotonic() + .5
        missing = sorted(set(clients)-active)
        print(f'Not ready: {args.target}' + (f'; waiting for {", ".join(missing)}' if missing else ''), flush=True)
        return 1
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    raise SystemExit(main())


## tools/validate_autonomy.py

#!/usr/bin/env python3
"""Simulator-only integration checks; isolated guard output cannot command motors."""
import copy
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import time
import yaml
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy, qos_profile_sensor_data
from geometry_msgs.msg import Twist
from lifecycle_msgs.srv import ChangeState, GetState
from nav_msgs.msg import OccupancyGrid, Odometry
from nav2_msgs.action import NavigateToPose
from sensor_msgs.msg import LaserScan

ws=Path('/home/robot/vacuum_ws')
logs=ws/'validation/autonomy-20261006'
logs.mkdir(parents=True,exist_ok=True)
processes=[]
handles=[]
def start(name,args):
    log=(logs/(name+'.log')).open('w')
    handles.append(log)
    p=subprocess.Popen(args,cwd=ws,stdout=log,stderr=subprocess.STDOUT,
                       stdin=subprocess.DEVNULL,start_new_session=True)
    processes.append(p)
    return p

def cleanup():
    for p in reversed(processes):
        try:
            os.killpg(p.pid,signal.SIGINT)
            p.wait(timeout=8)
        except (ProcessLookupError,subprocess.TimeoutExpired):
            pass
        try:
            os.killpg(p.pid,signal.SIGTERM)
            p.wait(timeout=2)
        except (ProcessLookupError,subprocess.TimeoutExpired):
            pass
    for log in handles:
        log.close()

rclpy.init()
node=Node('vacuum_autonomy_validation',parameter_overrides=[rclpy.parameter.Parameter('use_sim_time',value=True)])
maps=[]
odom=[]
subscriptions=[
    node.create_subscription(OccupancyGrid,'/map',maps.append,QoSProfile(depth=1,durability=DurabilityPolicy.TRANSIENT_LOCAL,reliability=ReliabilityPolicy.RELIABLE)),
    node.create_subscription(Odometry,'/odom',odom.append,qos_profile_sensor_data)]
client=ActionClient(node,NavigateToPose,'/navigate_to_pose')
result={'date':'2026-10-06','scope':'Ubuntu vacuum simulator only','tests':{}}
def wait(predicate,seconds):
    end=time.monotonic()+seconds
    while not predicate() and time.monotonic()<end:
        rclpy.spin_once(node,timeout_sec=0.05)
    return predicate()
def goal(x,y,timeout=90):
    request=NavigateToPose.Goal()
    request.pose.header.frame_id='map'
    request.pose.header.stamp=node.get_clock().now().to_msg()
    request.pose.pose.position.x=x
    request.pose.pose.position.y=y
    request.pose.pose.orientation.w=1.0
    future=client.send_goal_async(request)
    assert wait(future.done,10),'Goal submission timed out'
    handle=future.result()
    assert handle and handle.accepted,'Goal rejected'
    future=handle.get_result_async()
    if not wait(future.done,timeout):
        cancellation=handle.cancel_goal_async()
        wait(cancellation.done,5)
        raise RuntimeError('Goal timed out and was cancelled')
    return future.result()

try:
    start('sim',['python3','tools/run_sim.py','gui:=false','rviz:=false'])
    assert wait(lambda: bool(odom),40),'Simulator odometry unavailable'
    start('mapping',['ros2','launch','vacuum_sim','mapping.launch.py'])
    assert wait(lambda: bool(maps),30),'SLAM map unavailable'
    start('navigation',['ros2','launch','vacuum_sim','navigation.launch.py',
          'params_file:='+str(ws/'src/vacuum_sim/config/vacuum_nav2.yaml')])
    assert client.wait_for_server(timeout_sec=40),'Nav2 action endpoint unavailable'
    for name in ('bt_navigator','controller_server','planner_server','collision_monitor'):
        service=node.create_client(GetState,'/'+name+'/get_state')
        assert service.wait_for_service(timeout_sec=20),name+' lifecycle unavailable'
        deadline=time.monotonic()+40
        active=False
        while time.monotonic()<deadline:
            state=service.call_async(GetState.Request())
            if wait(state.done,3) and state.result().current_state.id==3:
                active=True
                break
            end=time.monotonic()+.3
            while time.monotonic()<end:
                rclpy.spin_once(node,timeout_sec=.05)
        assert active,name+' never activated'
    outcome=goal(1.0,0.0)
    assert outcome.status==4 and outcome.result.error_code==0, str(outcome)
    result['tests']['free_space_goal']={'status':outcome.status,'error_code':outcome.result.error_code}
    before=copy.deepcopy(odom[-1].pose.pose.position)
    outcome=goal(3.15,0.0,40)
    assert outcome.status==6,'Goal beyond room wall should abort'
    end=time.monotonic()+2
    while time.monotonic()<end:
        rclpy.spin_once(node,timeout_sec=.05)
    after=odom[-1].pose.pose.position
    movement=math.hypot(after.x-before.x,after.y-before.y)
    assert movement<.10 and abs(odom[-1].twist.twist.linear.x)<.02,'Robot moved toward blocked wall goal'
    result['tests']['goal_beyond_wall']={'status':outcome.status,'movement_m':movement}

    # An isolated copy of the exact configured collision guard. Its output has no
    # connection to the robot's /cmd_vel adapter; only synthetic scans are injected.
    p=copy.deepcopy(yaml.safe_load((ws/'src/vacuum_sim/config/vacuum_nav2.yaml').read_text())['collision_monitor']['ros__parameters'])
    p.update(cmd_vel_in_topic='/autonomy_guard_test/input',cmd_vel_out_topic='/autonomy_guard_test/output',
             state_topic='/autonomy_guard_test/state',polygons=['StopZone','SlowZone'])
    p['scan']['topic']='/autonomy_guard_test/scan'
    p['StopZone']['polygon_pub_topic']='/autonomy_guard_test/stop_polygon'
    p['SlowZone']['polygon_pub_topic']='/autonomy_guard_test/slow_polygon'
    guardfile=logs/'isolated_guard.yaml'
    guardfile.write_text(yaml.safe_dump({'/autonomy_guard_test/collision_monitor':{'ros__parameters':p}}))
    start('isolated_guard',['/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor','--ros-args',
                           '-r','__ns:=/autonomy_guard_test','--params-file',str(guardfile)])
    service=node.create_client(ChangeState,'/autonomy_guard_test/collision_monitor/change_state')
    assert service.wait_for_service(timeout_sec=15),'Guard service unavailable'
    for transition in (1,3):
        request=ChangeState.Request()
        request.transition.id=transition
        future=service.call_async(request)
        assert wait(future.done,10) and future.result().success,'Guard lifecycle transition failed'
    outputs=[]
    subscriptions.append(node.create_subscription(Twist,'/autonomy_guard_test/output',outputs.append,10))
    command=node.create_publisher(Twist,'/autonomy_guard_test/input',10)
    scans=node.create_publisher(LaserScan,'/autonomy_guard_test/scan',qos_profile_sensor_data)
    def exercise(distance,seconds=1.5):
        start_count=len(outputs)
        started=time.monotonic()
        start_sim=node.get_clock().now().nanoseconds
        end=started+(15 if distance is None else seconds)
        next_pub=0
        while time.monotonic()<end:
            if distance is None and node.get_clock().now().nanoseconds-start_sim>1_500_000_000:
                break
            if time.monotonic()>=next_pub:
                twist=Twist(); twist.linear.x=.20
                command.publish(twist)
                if distance is not None:
                    scan=LaserScan()
                    scan.header.frame_id='base_footprint'
                    scan.header.stamp=node.get_clock().now().to_msg()
                    scan.angle_min=-.01; scan.angle_max=.01; scan.angle_increment=.01
                    scan.range_min=.08; scan.range_max=12.; scan.ranges=[distance]*3
                    scans.publish(scan)
                next_pub=time.monotonic()+.05
            rclpy.spin_once(node,timeout_sec=.02)
        assert len(outputs)>start_count,'Guard published no output'
        elapsed_sim=(node.get_clock().now().nanoseconds-start_sim)*1e-9
        print('guard phase',distance,'simulation seconds',elapsed_sim,'output',outputs[-1].linear.x,flush=True)
        if distance is None:
            assert elapsed_sim>1.0,'Simulator clock did not advance enough for source-timeout test'
        return outputs[-1].linear.x
    clear=exercise(float('inf'))
    slow=exercise(.30)
    stop=exercise(.18)
    # Make the preceding valid scan clear so stopping below proves data timeout.
    exercise(float('inf'))
    stale=exercise(None,2)
    assert abs(clear-.20)<.01 and abs(slow-.08)<.01 and abs(stop)<.001 and abs(stale)<.001,(clear,slow,stop,stale)
    result['tests']['isolated_guard']={'clear_m_s':clear,'slow_m_s':slow,'stop_m_s':stop,'scan_timeout_m_s':stale}
    result['passed']=True
    print(json.dumps(result,indent=2),flush=True)
except Exception as error:
    result['passed']=False
    result['error']=str(error)
    print(json.dumps(result,indent=2),flush=True)
    raise
finally:
    (logs/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    cleanup()
    node.destroy_node()
    rclpy.shutdown()


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


## tools/build_furnished_room.py

"""Build original, local room assets. Standard library only; no model downloads.

Meshes are batched by furniture item/material; physics uses simple proxies.
All dimensions are metres. Generated assets live inside the simulator package.
"""
from collections import defaultdict
import math
from pathlib import Path
import random
import struct
import xml.etree.ElementTree as ET
import zlib

PACKAGE = Path('/home/robot/vacuum_ws/src/vacuum_sim')
ASSETS = PACKAGE / 'worlds/furnished'
ASSETS.mkdir(parents=True, exist_ok=True)
DAE = 'http://www.collada.org/2005/11/COLLADASchema'


def png(name, size, pixel):
    width, height = size
    raw = bytearray()
    for y in range(height):
        raw.append(0)
        for x in range(width):
            raw.extend(max(0, min(255, int(v))) for v in pixel(x, y))
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    (ASSETS / name).write_bytes(b'\x89PNG\r\n\x1a\n' +
        chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)) +
        chunk(b'IDAT', zlib.compress(bytes(raw), 7)) + chunk(b'IEND', b''))


def oak(x, y):
    plank = y // 48
    seam = y % 48 == 0 or (x + (plank % 3)*128) % 384 == 0
    if seam:
        return (132, 101, 68)
    grain = 5*math.sin(y*.65 + math.sin(x*.004)*4) + 2*math.sin(y*2+x*.015)
    shade = ((plank*17) % 13)-6 + grain + 2*math.sin(x*.03)
    return (181+shade, 139+shade, 94+shade*.7)


def fabric(x, y):
    grain = (x % 3 == 0)*7 - (y % 3 == 0)*5 + 2*math.sin(x*1.7+y*.8)
    return (184+grain, 169+grain, 145+grain)


def rug(x, y):
    edge = min(x, y, 511-x, 511-y)
    grain = ((x*7+y*13) % 11)-5
    stripe = edge < 12 or (22 < edge < 26) or (abs(x-256)+abs(y-256)) % 96 < 3
    return tuple(v+grain for v in ((65, 83, 86) if stripe else (201, 187, 157)))


def artwork(x, y):
    # An original abstract landscape, also used on the TV display.
    if (x-368)**2+(y-94)**2 < 37**2:
        return (239, 172, 102)
    if y > 194 + 31*math.sin(x*.009):
        return (42, 78, 83)
    if y > 150 + 38*math.sin(x*.011+1.4):
        return (71, 107, 112)
    return (174-y*.12, 199-y*.09, 204-y*.06)


def garden(x,y):
    if y > 275 + 22*math.sin(x*.009):return (102,126,73)
    if y > 244 + 18*math.sin(x*.014+.8):return (129,151,104)
    for cx,cy,r in ((80,212,90),(230,190,75),(710,200,110),(948,190,100)):
        if (x-cx)**2+(y-cy)**2<r*r:return (74+y*.09,112+y*.08,76+y*.05)
    cloud=math.exp(-((x-450)/180)**2-((y-86)/30)**2)+math.exp(-((x-750)/130)**2-((y-66)/22)**2)
    return (163+cloud*45+y*.06,196+cloud*25+y*.04,213+cloud*15)


png('oak.png', (2048, 2048), oak)
png('linen.png', (256, 256), fabric)
png('woven-rug.png', (512, 512), rug)
png('landscape.png', (512, 256), artwork)
png('garden.png', (1024,384), garden)

MATERIALS = {
    'oak': ((.62, .43, .25), 'oak.png'),
    'linen': ((.73, .66, .55), 'linen.png'),
    'rug': ((.76, .71, .61), 'woven-rug.png'),
    'art': ((.5, .65, .7), 'landscape.png'),
    'garden': ((.7,.8,.7), 'garden.png'),
    'plaster': ((.86, .85, .80), None),
    'sage': ((.30, .42, .36), None),
    'white': ((.92, .90, .85), None),
    'teal': ((.16, .32, .34), None),
    'terra': ((.62, .27, .15), None),
    'brass': ((.63, .48, .24), None),
    'charcoal': ((.035, .045, .05), None),
    'ceramic': ((.77, .81, .77), None),
    'leaf': ((.10, .29, .11), None),
    'leaf_light': ((.22, .40, .16), None),
    'blue': ((.22, .35, .48), None),
    'burgundy': ((.40, .13, .17), None),
}


def rotate(point, yaw):
    x, y, z = point
    return (x*math.cos(yaw)-y*math.sin(yaw), x*math.sin(yaw)+y*math.cos(yaw), z)


class Mesh:
    def __init__(self):
        self.faces = defaultdict(list)

    def triangle(self, material, points, uvs=None, normals=None):
        if uvs is None:
            uvs = [(p[0]*2, p[1]*2+p[2]*2) for p in points]
        a, b, c = points
        u = tuple(b[i]-a[i] for i in range(3)); v = tuple(c[i]-a[i] for i in range(3))
        n = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
        length = math.sqrt(sum(t*t for t in n))
        if length < 1e-10:
            return
        normal = tuple(t/length for t in n)
        self.faces[material].append((points, normals or [normal]*3, uvs))

    def quad(self, material, points, uvs=None, normals=None):
        if uvs is None:
            uvs = [(p[0]*2, p[1]*2+p[2]*2) for p in points]
        for indices in ((0, 1, 2), (0, 2, 3)):
            self.triangle(material, [points[i] for i in indices], [uvs[i] for i in indices],
                          [normals[i] for i in indices] if normals else None)

    def box(self, center, size, material, yaw=0, floor_uv=False):
        points = []
        for x, y, z in ((-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),
                        (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)):
            q = rotate((x*size[0]/2, y*size[1]/2, z*size[2]/2), yaw)
            points.append(tuple(q[i]+center[i] for i in range(3)))
        for face in ((0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)):
            p = [points[i] for i in face]
            uv = [((q[0]+4)/8,(q[1]+3.5)/7) for q in p] if floor_uv else None
            self.quad(material, p, uv)

    def rounded(self, center, size, radius, material, yaw=0):
        """Bevelled upholstered/wood parts: four rounded corners, curved edges."""
        sx, sy, sz = size
        radius = min(radius, sx/3, sy/3, sz/3)
        rings = []; normal_rings=[]
        for zsign, tilt in ((-1,-math.pi/2),(-1,-math.pi/3),(-1,-math.pi/6),(-1,0),
                            (1,0),(1,math.pi/6),(1,math.pi/3),(1,math.pi/2)):
            z=zsign*(sz/2-radius)+radius*math.sin(tilt)
            ring = []; normal_ring=[]
            for cx, cy, start in ((1,1,0),(-1,1,90),(-1,-1,180),(1,-1,270)):
                for j in range(5):
                    angle = math.radians(start+j*90/4)
                    r = max(.0001, radius*math.cos(tilt))
                    q = rotate((cx*(sx/2-radius)+r*math.cos(angle),
                                cy*(sy/2-radius)+r*math.sin(angle), z), yaw)
                    ring.append(tuple(q[i]+center[i] for i in range(3)))
                    normal_ring.append(rotate((math.cos(angle)*math.cos(tilt),math.sin(angle)*math.cos(tilt),math.sin(tilt)),yaw))
            rings.append(ring)
            normal_rings.append(normal_ring)
        count = len(rings[0])
        for layer,(lower, upper) in enumerate(zip(rings, rings[1:])):
            for j in range(count):
                k = (j+1) % count
                self.quad(material, [lower[j],lower[k],upper[k],upper[j]],
                          normals=[normal_rings[layer][j],normal_rings[layer][k],normal_rings[layer+1][k],normal_rings[layer+1][j]])
        for j in range(1,count-1):
            self.triangle(material, [rings[0][0],rings[0][j+1],rings[0][j]])
            self.triangle(material, [rings[-1][0],rings[-1][j],rings[-1][j+1]])

    def lathe(self, center, profile, material, segments=24):
        rings = [[(center[0]+r*math.cos(i*2*math.pi/segments),
                   center[1]+r*math.sin(i*2*math.pi/segments),center[2]+z)
                  for i in range(segments)] for r,z in profile]
        for lower,upper in zip(rings,rings[1:]):
            for i in range(segments):
                j=(i+1)%segments
                self.quad(material,[lower[i],lower[j],upper[j],upper[i]])
        for ring,reverse in ((rings[0],True),(rings[-1],False)):
            for i in range(1,segments-1):
                self.triangle(material,[ring[0],ring[i+1],ring[i]] if reverse else [ring[0],ring[i],ring[i+1]])

    def cylinder(self, center, radius, height, material):
        self.lathe(center,[(radius,-height/2),(radius,height/2)],material)

    def leaf(self, center, length, width, yaw, material):
        coords=[(0,0,0),(-width,length*.35,length*.22),(0,length*.5,length*.45),
                (width,length*.35,length*.22),(0,length*.85,length*.45)]
        p=[tuple(rotate(q,yaw)[i]+center[i] for i in range(3)) for q in coords]
        for face in ((0,1,2),(0,2,3),(1,4,2),(2,4,3)):
            self.triangle(material,[p[i] for i in face])
            self.triangle(material,[p[i] for i in reversed(face)])

    def save(self, name):
        root=ET.Element('COLLADA', xmlns=DAE, version='1.4.1')
        asset=ET.SubElement(root,'asset')
        ET.SubElement(asset,'unit',name='meter',meter='1')
        ET.SubElement(asset,'up_axis').text='Z_UP'
        images=ET.SubElement(root,'library_images'); effects=ET.SubElement(root,'library_effects')
        mats=ET.SubElement(root,'library_materials'); geometries=ET.SubElement(root,'library_geometries')
        scenes=ET.SubElement(root,'library_visual_scenes'); scene=ET.SubElement(scenes,'visual_scene',id='Scene',name='Scene')
        for mat,faces in self.faces.items():
            color,texture=MATERIALS[mat]
            effect=ET.SubElement(effects,'effect',id=mat+'fx'); profile=ET.SubElement(effect,'profile_COMMON')
            if texture:
                im=ET.SubElement(images,'image',id=mat+'image');ET.SubElement(im,'init_from').text=texture
                par=ET.SubElement(profile,'newparam',sid=mat+'surface'); surf=ET.SubElement(par,'surface',type='2D');ET.SubElement(surf,'init_from').text=mat+'image'
                par=ET.SubElement(profile,'newparam',sid=mat+'sampler');sample=ET.SubElement(par,'sampler2D');ET.SubElement(sample,'source').text=mat+'surface'
            phong=ET.SubElement(ET.SubElement(profile,'technique',sid='common'),'phong')
            ET.SubElement(ET.SubElement(phong,'ambient'),'color').text=' '.join(str(v*.7) for v in color)+' 1'
            diffuse=ET.SubElement(phong,'diffuse')
            if texture:ET.SubElement(diffuse,'texture',texture=mat+'sampler',texcoord='UVSET0')
            else:ET.SubElement(diffuse,'color').text=' '.join(map(str,color))+' 1'
            spec=.22 if mat=='brass' else .03
            ET.SubElement(ET.SubElement(phong,'specular'),'color').text=f'{spec} {spec} {spec} 1'
            ET.SubElement(ET.SubElement(phong,'shininess'),'float').text='20'
            material=ET.SubElement(mats,'material',id=mat,name=mat);ET.SubElement(material,'instance_effect',url='#'+mat+'fx')
            mesh=ET.SubElement(ET.SubElement(geometries,'geometry',id=mat+'mesh',name=mat),'mesh')
            positions=[];normals=[];uv=[]
            for points,ns,tex in faces:
                for p,t,n in zip(points,tex,ns): positions.extend(p);normals.extend(n);uv.extend(t)
            def source(sid,values,stride,params):
                src=ET.SubElement(mesh,'source',id=sid)
                ET.SubElement(src,'float_array',id=sid+'array',count=str(len(values))).text=' '.join(f'{v:.6f}' for v in values)
                accessor=ET.SubElement(ET.SubElement(src,'technique_common'),'accessor',source='#'+sid+'array',count=str(len(values)//stride),stride=str(stride))
                for param in params:ET.SubElement(accessor,'param',name=param,type='float')
            source(mat+'pos',positions,3,('X','Y','Z'));source(mat+'norm',normals,3,('X','Y','Z'));source(mat+'uv',uv,2,('S','T'))
            vertices=ET.SubElement(mesh,'vertices',id=mat+'verts');ET.SubElement(vertices,'input',semantic='POSITION',source='#'+mat+'pos')
            triangles=ET.SubElement(mesh,'triangles',material=mat,count=str(len(faces)))
            for semantic,src,offset in [('VERTEX',mat+'verts',0),('NORMAL',mat+'norm',1),('TEXCOORD',mat+'uv',2)]:
                ET.SubElement(triangles,'input',semantic=semantic,source='#'+src,offset=str(offset),**({'set':'0'} if offset==2 else {}))
            ET.SubElement(triangles,'p').text=' '.join(f'{i} {i} {i}' for i in range(len(positions)//3))
            node=ET.SubElement(scene,'node',id=mat+'node',name=mat,type='NODE')
            inst=ET.SubElement(node,'instance_geometry',url='#'+mat+'mesh')
            bind=ET.SubElement(ET.SubElement(inst,'bind_material'),'technique_common')
            im=ET.SubElement(bind,'instance_material',symbol=mat,target='#'+mat)
            ET.SubElement(im,'bind_vertex_input',semantic='UVSET0',input_semantic='TEXCOORD',input_set='0')
        ET.SubElement(ET.SubElement(root,'scene'),'instance_visual_scene',url='#Scene')
        path=ASSETS/(name+'.dae'); ET.ElementTree(root).write(path,encoding='utf-8',xml_declaration=True)
        return path


room_mesh = Mesh()
root=ET.Element('sdf',version='1.9');world=ET.SubElement(root,'world',name='vacuum_room')
def element(parent,tag,value):ET.SubElement(parent,tag).text=str(value)
physics=ET.SubElement(world,'physics',name='physics',type='ignored')
element(physics,'max_step_size','0.005555555555555556');element(physics,'real_time_factor',1.)
element(world,'gravity','0 0 -9.81')
for filename,classname in [('physics','Physics'),('user-commands','UserCommands'),('scene-broadcaster','SceneBroadcaster'),('sensors','Sensors')]:
    plugin=ET.SubElement(world,'plugin',filename='gz-sim-'+filename+'-system',name='gz::sim::systems::'+classname)
    if classname=='Sensors':element(plugin,'render_engine','ogre2')
scene=ET.SubElement(world,'scene');element(scene,'ambient','.7 .7 .7 1');element(scene,'background','.69 .79 .85 1');element(scene,'shadows','false')
light=ET.SubElement(world,'light',name='afternoon_daylight',type='directional')
element(light,'pose','0 0 6 0 0 0');element(light,'diffuse','.75 .72 .65 1');element(light,'specular','.15 .15 .15 1');element(light,'direction','-.5 -.4 -1');element(light,'cast_shadows','false')
light=ET.SubElement(world,'light',name='soft_window_fill',type='directional')
element(light,'pose','0 0 6 0 0 0');element(light,'diffuse','.25 .28 .3 1');element(light,'specular','0 0 0 1');element(light,'direction','.4 .4 -1');element(light,'cast_shadows','false')
gui=ET.SubElement(world,'gui',fullscreen='false')
# Main Gazebo window opens with a useful architectural view.
camera=ET.SubElement(gui,'camera',name='user_camera');element(camera,'pose','7 -9 8 0 .60 2.2')
room_model=ET.SubElement(world,'model',name='furnished_living_room');element(room_model,'static','true')
element(room_model,'self_collide','false')
room_link=ET.SubElement(room_model,'link',name='room')


class Item:
    def __init__(self,name,pose=(0,0,0,0)):
        self.name=name;self.mesh=Mesh();self.collisions=[];self.pose=pose
    def box(self,center,size,material,yaw=0,collision=False,rounded=0):
        if rounded:self.mesh.rounded(center,size,rounded,material,yaw)
        else:self.mesh.box(center,size,material,yaw)
        if collision:self.collisions.append(('box',center,size,yaw))
    def cylinder(self,center,radius,height,material,collision=False):
        self.mesh.cylinder(center,radius,height,material)
        if collision:self.collisions.append(('cylinder',center,(radius,height),0))
    def save(self):
        # One shared visual mesh gives the renderer one draw batch per material,
        # rather than repeating material/draw setup for each piece of furniture.
        x,y,z,yaw=self.pose
        for material,faces in self.mesh.faces.items():
            for points,normals,uvs in faces:
                transformed=[]
                for point in points:
                    q=rotate(point,yaw);transformed.append((q[0]+x,q[1]+y,q[2]+z))
                room_mesh.faces[material].append((transformed,[rotate(n,yaw) for n in normals],uvs))
        # All fixed furnishings are shapes of one immobile body. This prevents
        # expensive contact checks between the floor and static furniture.
        for i,(kind,center,size,local_yaw) in enumerate(self.collisions):
            q=rotate(center,yaw);center=(q[0]+x,q[1]+y,q[2]+z)
            collision=ET.SubElement(room_link,'collision',name=self.name+'_proxy'+str(i));element(collision,'pose',' '.join(map(str,center))+f' 0 0 {yaw+local_yaw}')
            shape=ET.SubElement(ET.SubElement(collision,'geometry'),kind)
            if kind=='box':element(shape,'size',' '.join(map(str,size)))
            else:element(shape,'radius',size[0]);element(shape,'length',size[1])


house=Item('architecture')
house.mesh.box((0,0,-.04),(8.2,7.2,.08),'oak',floor_uv=True)
house.collisions.append(('box',(0,0,-.04),(8.2,7.2,.08),0))
# North wall has a real window opening. Collision proxies match the wall pieces.
for center,size in [((0,-3.5,1.4),(8.2,.12,2.8)),((-4,0,1.4),(.12,7,2.8)),((4,0,1.4),(.12,7,2.8)),
                    ((0,3.5,.45),(8.2,.12,.9)),((0,3.5,2.65),(8.2,.12,.3)),
                    ((-3.15,3.5,1.7),(1.9,.12,1.6)),((3.15,3.5,1.7),(1.9,.12,1.6))]:
    house.box(center,size,'sage' if center[0]==4 else 'plaster',collision=True)
for x in (-4,4):house.box((x*.985,0,.055),(.035,6.95,.11),'white')
for y in (-3.5,3.5):house.box((0,y*.985,.055),(7.95,.035,.11),'white')
for x in (-2.19,0,2.19):house.box((x,3.48,1.7),(.055,.15,1.6),'white')
for z in (.9,1.7,2.5):house.box((0,3.48,z),(4.45,.16,.055),'white')
house.box((0,3.35,.88),(4.65,.40,.055),'oak')
house.mesh.quad('garden',[(-2.20,3.62,.90),(2.20,3.62,.90),(2.20,3.62,2.50),(-2.20,3.62,2.50)],[(0,0),(1,0),(1,1),(0,1)])
# Curtains, hung above floor clearance, with visible folds.
for side in (-1,1):
    for i in range(12):house.cylinder((side*2.25+(i-5.5)*.025,3.28,1.6),.029,2.05,'linen')
house.box((-2.5,-3.425,1.04),(.94,.035,2.05),'oak')
house.box((-2.5,-3.395,1.04),(1.02,.025,2.13),'white')
house.box((-2.5,-3.36,1.04),(.90,.025,2.01),'oak')
house.cylinder((-2.18,-3.32,1.03),.025,.05,'brass')
house.save()

sofa=Item('three_seat_sofa',(-.65,2.72,0,0))
sofa.box((0,0,.28),(2.55,.90,.30),'teal',collision=True,rounded=.06)
sofa.box((0,.36,.65),(2.55,.21,.75),'teal',collision=True,rounded=.045)
for x in (-1.21,1.21):sofa.box((x,-.03,.53),(.18,.87,.56),'teal',collision=True,rounded=.035)
for x in (-.77,0,.77):
    sofa.box((x,-.08,.49),(.72,.65,.18),'linen',rounded=.05)
    sofa.box((x,.24,.74),(.70,.15,.44),'teal',rounded=.04)
for x,y in ((-1.08,-.30),(1.08,-.30),(-1.08,.30),(1.08,.30)):
    sofa.cylinder((x,y,.09),.035,.18,'oak',collision=True)
for x,mat,yaw in ((-.94,'terra',.18),(.88,'linen',-.2)):
    sofa.box((x,.10,.72),(.38,.22,.38),mat,yaw=yaw,rounded=.06)
sofa.save()

carpet=Item('woven_living_room_rug',(-.65,1.1,0,0))
# A flush decorative rug is deliberately not a raised lidar-invisible obstacle.
carpet.mesh.quad('rug',[(-1.6,-1.15,.002),(1.6,-1.15,.002),(1.6,1.15,.002),(-1.6,1.15,.002)],[(0,0),(1,0),(1,1),(0,1)])
carpet.save()

coffee=Item('rounded_coffee_table',(-.65,1.32,0,0))
coffee.box((0,0,.40),(1.25,.63,.07),'oak',collision=True,rounded=.018)
for x in (-.47,.47):
    for y in (-.21,.21):coffee.cylinder((x,y,.20),.035,.40,'charcoal',collision=True)
coffee.box((-.20,0,.45),(.28,.20,.025),'burgundy')
coffee.box((-.18,.01,.47),(.25,.18,.022),'white')
coffee.mesh.lathe((.29,.02,.44),[(.045,0),(.048,.08),(.046,.085)],'ceramic')
coffee.save()

console=Item('oak_media_console',(3.65,.70,0,0))
console.box((0,0,.35),(.45,2.05,.51),'oak',collision=True,rounded=.012)
for y in (-.67,0,.67):
    console.box((-.235,y,.35),(.02,.64,.42),'oak')
    console.box((-.251,y,.50),(.016,.16,.009),'brass')
for y in (-.82,.82):console.cylinder((0,y,.075),.035,.15,'charcoal',collision=True)
console.box((.05,0,1.37),(.04,1.65,.96),'charcoal')
console.mesh.quad('art',[(.025,.79,.93),(.025,-.79,.93),(.025,-.79,1.81),(.025,.79,1.81)],[(0,0),(1,0),(1,1),(0,1)])
for y in (-.88,.88):console.cylinder((0,y,.70),.045,.20,'charcoal')
console.save()

bookshelf=Item('bookcase',(-3.7,1.55,0,0))
bookshelf.box((.08,0,.105),(.42,1.20,.21),'oak',collision=True)
bookshelf.box((-.05,0,1.05),(.12,1.20,2.1),'oak',collision=True)
for y in (-.57,.57):bookshelf.box((.08,y,1.05),(.42,.045,2.1),'oak',collision=True)
for z in (.06,.50,.96,1.42,1.88,2.12):bookshelf.box((.08,0,z),(.42,1.2,.035),'oak',collision=True)
rng=random.Random(17)
for row,z in enumerate((.50,.96,1.42)):
    for i in range(12):
        y=-.48+i*.073; h=rng.uniform(.22,.34)
        bookshelf.box((.13,y,z+.018+h/2),(.22,.055,h),rng.choice(['terra','blue','burgundy','white','teal']))
bookshelf.mesh.lathe((.10,-.22,1.90),[(.065,0),(.08,.09),(.045,.23),(.035,.25)],'ceramic')
bookshelf.box((.15,.32,1.96),(.18,.25,.08),'linen')
bookshelf.save()

dining=Item('dining_table',(-2.4,-1.55,0,0))
dining.box((0,0,.76),(1.45,.88,.065),'oak',collision=True,rounded=.02)
for x in (-.58,.58):
    for y in (-.30,.30):dining.cylinder((x,y,.37),.045,.74,'oak',collision=True)
for x in (-.35,.35):
    dining.cylinder((x,0,.804),.14,.014,'ceramic')
dining.mesh.lathe((0,0,.80),[(.05,0),(.09,.07),(.055,.21)],'terra')
dining.save()

def chair(name,pose):
    item=Item(name,pose)
    item.box((0,0,.45),(.45,.45,.065),'linen',collision=True,rounded=.02)
    item.box((0,.195,.72),(.46,.065,.50),'oak',collision=True,rounded=.015)
    for x in (-.16,.16):
        for y in (-.16,.16):item.cylinder((x,y,.225),.025,.45,'oak',collision=True)
    item.save()
for n,x,y,yaw in [('north',-2.4,-.78,math.pi),('south',-2.4,-2.33,0),('west',-3.47,-1.55,-math.pi/2)]:
    chair('dining_chair_'+n,(x,y,0,yaw))

desk=Item('home_office_desk',(2.20,-2.95,0,0))
desk.box((0,0,.76),(1.65,.65,.055),'oak',collision=True,rounded=.015)
for x in (-.70,.70):
    for y in (-.23,.23):desk.box((x,y,.37),(.045,.045,.74),'charcoal',collision=True)
desk.box((.0,-.17,1.10),(.67,.035,.40),'charcoal')
desk.mesh.quad('art',[(.30,-.149,.925),(-.30,-.149,.925),(-.30,-.149,1.275),(.30,-.149,1.275)],[(0,0),(1,0),(1,1),(0,1)])
desk.box((0,-.17,.90),(.04,.05,.24),'charcoal')
desk.box((0,-.10,.805),(.25,.20,.025),'charcoal')
desk.box((0,.09,.805),(.43,.14,.016),'charcoal')
for y in (-.04,.0,.04):
    for x in range(14):desk.box((-.19+x*.028,y+.08,.816),(.021,.022,.004),'white')
desk.box((.58,.04,.812),(.14,.18,.024),'blue',rounded=.007)
desk.save()
chair('office_chair',(2.2,-2.10,0,math.pi))

lamp=Item('floor_lamp',(1.30,2.72,0,0))
lamp.cylinder((0,0,.105),.20,.21,'charcoal',collision=True)
lamp.cylinder((0,0,.77),.018,1.5,'brass',collision=True)
lamp.mesh.lathe((0,0,1.40),[(.28,0),(.21,.36)],'linen')
lamp.save()

def plant(name,pose,height):
    item=Item(name,pose)
    item.mesh.lathe((0,0,0),[(.16,0),(.21,.32),(.22,.34),(.20,.36)],'terra')
    item.collisions.append(('cylinder',(0,0,.18),(.22,.36),0))
    item.cylinder((0,0,.34+height*.35),.012,height*.7,'oak')
    for i in range(22):
        angle=i*2.399; radius=.03+(i%4)*.035
        z=.33+(i%7)*height/9
        item.mesh.leaf((radius*math.cos(angle),radius*math.sin(angle),z),height*.43,.09,angle,'leaf' if i%2 else 'leaf_light')
    item.save()
plant('window_plant',(2.90,2.82,0,0),1.20)
plant('entry_plant',(-3.45,-2.87,0,0),.72)

art=Item('framed_wall_art')
for x in (-.75,.40):
    art.box((x,-3.42,1.70),(.78,.04,1.04),'oak')
    art.mesh.quad('art',[(x+.35,-3.39,1.22),(x-.35,-3.39,1.22),(x-.35,-3.39,2.18),(x+.35,-3.39,2.18)],[(0,0),(1,0),(1,1),(0,1)])
art.save()

path=room_mesh.save('living_room')
visual=ET.SubElement(room_link,'visual',name='furnished_room');geometry=ET.SubElement(visual,'geometry')
element(ET.SubElement(geometry,'mesh'),'uri',str(path));element(visual,'cast_shadows','false')

ET.indent(root,space='  ')
ET.ElementTree(root).write(PACKAGE/'worlds/room.sdf',encoding='utf-8',xml_declaration=True)
print(f'Furnished 8 x 7 m room: one fixed body, {len(room_link.findall("collision"))} collision shapes, batched materials.')


## tools/validate_directional_guard.py

"""Exercise the exact drive guard in an isolated namespace, with no motor output."""
import copy
import json
import math
from pathlib import Path
import subprocess
import time
import yaml
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from lifecycle_msgs.srv import ChangeState

WS=Path('/home/robot/vacuum_ws')
OUT=WS/'validation/furnished-20261007'
OUT.mkdir(parents=True,exist_ok=True)
p=copy.deepcopy(yaml.safe_load((WS/'.lab/drive-guard.yaml').read_text())['collision_monitor']['ros__parameters'])
p.update(cmd_vel_in_topic='/furnished_guard_test/input',cmd_vel_out_topic='/furnished_guard_test/output',state_topic='/furnished_guard_test/state')
p['scan']['topic']='/furnished_guard_test/scan'
for key in ('StopZone','SlowZone'):p[key]['polygon_pub_topic']='/furnished_guard_test/'+key
config=OUT/'isolated-guard.yaml'
config.write_text(yaml.safe_dump({'/furnished_guard_test/collision_monitor':{'ros__parameters':p}}))
rclpy.init()
node=Node('furnished_guard_validation',parameter_overrides=[Parameter('use_sim_time',value=True)])
outputs=[]
node.create_subscription(Twist,'/furnished_guard_test/output',outputs.append,10)
pub=node.create_publisher(Twist,'/furnished_guard_test/input',10)
scans=node.create_publisher(LaserScan,'/furnished_guard_test/scan',qos_profile_sensor_data)
service=node.create_client(ChangeState,'/furnished_guard_test/collision_monitor/change_state')
log=(OUT/'isolated-guard.log').open('w')
proc=subprocess.Popen(['/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor','--ros-args','-r','__ns:=/furnished_guard_test','--params-file',str(config)],stdout=log,stderr=subprocess.STDOUT)
report={'scope':'isolated test topics; no robot command output','tests':{}}


def wait(predicate,seconds):
    end=time.monotonic()+seconds
    while not predicate() and time.monotonic()<end:rclpy.spin_once(node,timeout_sec=.03)
    assert predicate(),'Timed out'


def exercise(label,speed,distance,angle=0):
    first=len(outputs);start=node.get_clock().now().nanoseconds
    end=time.monotonic()+5
    while time.monotonic()<end:
        cmd=Twist();cmd.linear.x=speed;pub.publish(cmd)
        if distance is not None:
            scan=LaserScan();scan.header.frame_id='base_footprint';scan.header.stamp=node.get_clock().now().to_msg()
            scan.angle_min=angle-.005;scan.angle_max=angle+.005;scan.angle_increment=.005
            scan.range_min=.03;scan.range_max=12.;scan.ranges=[distance]*3;scans.publish(scan)
        next_pub=time.monotonic()+.05
        while time.monotonic()<next_pub:rclpy.spin_once(node,timeout_sec=.01)
        if node.get_clock().now().nanoseconds-start>1_300_000_000 and len(outputs)>first:break
    assert len(outputs)>first,'No guard output'
    value=outputs[-1].linear.x
    report['tests'][label]=value
    print(label,value,flush=True)
    return value


try:
    assert service.wait_for_service(timeout_sec=15),'Guard lifecycle unavailable'
    for id in (1,3):
        req=ChangeState.Request();req.transition.id=id
        future=service.call_async(req);wait(future.done,10)
        assert future.result().success,'Lifecycle transition failed'
    wait(lambda: node.get_clock().now().nanoseconds>0,5)
    assert abs(exercise('clear_fast_forward',.5,float('inf'))-.5)<.01
    assert abs(exercise('forward_slow_front',.5,.70)-.20)<.01
    assert abs(exercise('forward_stop_front',.5,.35))<.001
    assert abs(exercise('reverse_away_from_front',-.3,.35)+.30)<.01
    assert abs(exercise('reverse_stop_rear',-.3,.39,math.pi))<.001
    assert abs(exercise('forward_away_from_rear',.5,.39,math.pi)-.50)<.01
    # Side point inside the padded body must block motion even when a directional
    # strip would miss it: the predictive footprint remains active.
    assert abs(exercise('padded_body_contact_stop',.5,.14,math.pi/2))<.001
    exercise('clear_before_timeout',.5,float('inf'))
    assert abs(exercise('stale_lidar_stop',.5,None))<.001
    report['passed']=True
finally:
    proc.terminate()
    try:proc.wait(timeout=8)
    except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=2)
    log.close();node.destroy_node();rclpy.shutdown()
    (OUT/'directional-guard.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)


## tools/validate_drive.py

"""Check camera delivery and forward/reverse movement in a running drive session."""
import json
import math
from pathlib import Path
import subprocess
import struct
import time
import zlib
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

WS = Path('/home/robot/vacuum_ws')
rclpy.init()
node = Node('vacuum_direct_drive_validation')
images = []
odom = []
commands = []
node.create_subscription(Odometry, '/odom', odom.append, qos_profile_sensor_data)
node.create_subscription(Twist, '/vacuum/selected_cmd_vel', commands.append, 10)
report = {'date': '2026-10-07', 'scope': 'simulator only', 'tests': {}}
bridge = None
latest_image = None


def remember_image(message):
    global latest_image
    latest_image = message
    images.append((time.monotonic(), message.header.stamp.sec + message.header.stamp.nanosec * 1e-9))


node.create_subscription(Image, '/camera/image_raw', remember_image, qos_profile_sensor_data)


def spin(seconds):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        rclpy.spin_once(node, timeout_sec=.03)


try:
    # Let the renderer and WSLg viewer settle after cold-start shader creation.
    spin(12)
    assert len(images) > 100 and odom, 'Camera or odometry unavailable'
    capture = images[-180:]
    fps_sim = (len(capture)-1) / (capture[-1][1]-capture[0][1])
    fps_wall = (len(capture)-1) / (capture[-1][0]-capture[0][0])
    report['tests']['camera'] = {'target_fps': 60, 'simulation_fps': fps_sim, 'wall_fps': fps_wall, 'frames': len(capture)}
    assert 57 <= fps_sim <= 63, f'Camera simulation frequency was {fps_sim}'
    assert fps_wall >= 55, f'Camera delivery too slow: {fps_wall}'
    log = (WS / '.lab/drive-validation-bridge.log').open('w')
    bridge = subprocess.Popen(['python3', 'tools/controller_bridge.py'], cwd=WS, text=True,
                              stdin=subprocess.PIPE, stdout=log, stderr=subprocess.STDOUT)

    def exercise(speed, held, seconds):
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            assert bridge.poll() is None, 'Input bridge exited'
            bridge.stdin.write(json.dumps({'v': speed, 'w': 0., 'held': held}) + '\n')
            bridge.stdin.flush()
            rclpy.spin_once(node, timeout_sec=.03)
            time.sleep(.02)

    exercise(0., False, 4)
    for label, speed, seconds in (('forward', .50, 2), ('reverse', -.30, 3)):
        before = odom[-1].pose.pose
        q = before.orientation
        yaw = math.atan2(2*(q.w*q.z + q.x*q.y), 1-2*(q.y*q.y+q.z*q.z))
        first = len(odom)
        exercise(speed, True, seconds)
        after = odom[-1].pose.pose.position
        displacement = (after.x-before.position.x)*math.cos(yaw) + (after.y-before.position.y)*math.sin(yaw)
        assert displacement * (1 if speed > 0 else -1) > .06, f'{label} did not move as expected: {displacement}'
        velocities = [m.twist.twist.linear.x for m in odom[first:]]
        actual_speed = max(velocities) if speed > 0 else min(velocities)
        assert abs(actual_speed) >= abs(speed)*.85, f'{label} speed clipped: {actual_speed}'
        report['tests'][label] = {'signed_displacement_m': displacement, 'peak_odometry_m_s': actual_speed}
        exercise(0., False, 2)
        assert abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02
    report['tests']['released_stop'] = True
    exercise(.1, True, 1)
    spin(2)
    assert abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02
    report['tests']['input_timeout_stop'] = True
    message = latest_image
    assert message.encoding in ('rgb8','bgr8'), message.encoding
    rows = []
    data = bytes(message.data)
    for y in range(message.height):
        row = data[y*message.step:y*message.step+message.width*3]
        if message.encoding == 'bgr8':
            row = bytes(v for i in range(0,len(row),3) for v in (row[i+2],row[i+1],row[i]))
        rows.append(b'\0'+row)
    def chunk(kind, content):
        return struct.pack('>I',len(content))+kind+content+struct.pack('>I',zlib.crc32(kind+content))
    png = b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',message.width,message.height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b''.join(rows)))+chunk(b'IEND',b'')
    (WS/'validation/furnished-robot-camera.png').write_bytes(png)
    report['passed'] = True
except Exception as exc:
    report['passed'] = False
    report['error'] = str(exc)
    raise
finally:
    if bridge:
        try:
            bridge.stdin.close()
            bridge.wait(timeout=5)
        except Exception:
            bridge.terminate()
    path = WS / 'validation/direct-drive-20261007'
    path.mkdir(parents=True, exist_ok=True)
    (path / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2), flush=True)
    node.destroy_node()
    rclpy.shutdown()


## tools/capture_room_preview.py

"""Temporarily add a camera to the running simulator and save a room overview."""
from pathlib import Path
import struct
import subprocess
import time
import zlib
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image

WS=Path('/home/robot/vacuum_ws')
out=WS/'validation/furnished-20261007';out.mkdir(parents=True,exist_ok=True)
sdf=out/'preview-camera.sdf'
sdf.write_text('''<sdf version="1.9"><model name="room_preview"><static>true</static>
<pose>-2.8 -2.6 5.5 0 0.92 0.748</pose><link name="camera">
<sensor name="overview" type="camera"><topic>/room_preview</topic><always_on>true</always_on><update_rate>1</update_rate>
<camera><horizontal_fov>1.6</horizontal_fov><image><width>1200</width><height>900</height><format>R8G8B8</format></image>
<clip><near>0.05</near><far>30</far></clip></camera></sensor></link></model></sdf>''')
rclpy.init();node=Node('furnished_room_preview_capture');images=[]
node.create_subscription(Image,'/room_preview',images.append,qos_profile_sensor_data)
bridge=None
created=False
try:
    result=subprocess.run(['/opt/ros/jazzy/lib/ros_gz_sim/create','-world','vacuum_room','-file',str(sdf),'-name','room_preview',
                           '-x','-2.8','-y','-2.6','-z','5.5','-R','0','-P','.92','-Y','.748'],capture_output=True,text=True,timeout=20)
    assert result.returncode==0,result.stdout+result.stderr
    created=True
    log=(out/'preview-bridge.log').open('w')
    bridge=subprocess.Popen(['/opt/ros/jazzy/lib/ros_gz_bridge/parameter_bridge','/room_preview@sensor_msgs/msg/Image[gz.msgs.Image'],stdout=log,stderr=subprocess.STDOUT)
    end=time.monotonic()+25
    while not images and time.monotonic()<end:rclpy.spin_once(node,timeout_sec=.1)
    assert images,'Preview camera did not publish'
    m=images[-1];assert m.encoding=='rgb8',m.encoding
    data=bytes(m.data);raw=b''.join(b'\0'+data[y*m.step:y*m.step+m.width*3] for y in range(m.height))
    def chunk(kind,data):return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data))
    png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',m.width,m.height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b'')
    path=out/'room-overview.png';path.write_bytes(png);print(path,flush=True)
finally:
    if bridge:
        bridge.terminate()
        try:bridge.wait(timeout=5)
        except subprocess.TimeoutExpired:bridge.kill();bridge.wait(timeout=2)
        log.close()
    if created:
        result=subprocess.run(['gz','service','-s','/world/vacuum_room/remove','--reqtype','gz.msgs.Entity','--reptype','gz.msgs.Boolean','--timeout','5000','--req','name: "room_preview", type: MODEL'],capture_output=True,text=True,timeout=8)
        print('Preview camera removal:',result.stdout.strip(),result.stderr.strip(),flush=True)
    node.destroy_node();rclpy.shutdown()


## tools/check_lab.py

"""Logic checks using installed ROS types; does not move the robot."""
import math
from pathlib import Path
import tempfile
import threading
import time
from types import SimpleNamespace
import unittest
from geometry_msgs.msg import Twist
import command_gate
import controller_bridge
from prepare_lab import circle


class Publisher:
    def __init__(self):
        self.messages = []

    def publish(self, message):
        self.messages.append(message)


class SafetyTests(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(controller_bridge.decode('{"v":100,"w":100,"held":true}'), (.50, 1.2))
        self.assertEqual(controller_bridge.decode('{"v":-100,"w":-100,"held":true}'), (-.30, -1.2))
        self.assertEqual(controller_bridge.decode('{"v":0.1,"w":0.2,"held":false}'), (0., 0.))
        with self.assertRaises(ValueError):
            controller_bridge.decode('{"v":"NaN","w":0,"held":true}')

    def test_manual_watchdog_and_interlock(self):
        from unittest.mock import patch
        fake = SimpleNamespace(pub=Publisher(), lock=threading.Lock(), latest=(.15, .5),
                               received=time.monotonic(), closed=False,
                               states={'collision_monitor': (3, time.monotonic())},
                               scan_at=time.monotonic(), motion_since=0.,
                               report=lambda *args: None)
        with patch.object(controller_bridge, 'MODE') as mode:
            mode.exists.return_value = True
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, .15)
            mode.exists.return_value = False
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
            mode.exists.return_value = True
            fake.received = time.monotonic() - .5
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
            fake.received = time.monotonic()
            fake.states['collision_monitor'] = (3, time.monotonic() - 2.)
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
            fake.states['collision_monitor'] = (3, time.monotonic())
            fake.scan_at = time.monotonic() - .6
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)

    def test_gate_mode_and_timeout(self):
        root = Path('/home/robot/vacuum_ws/.lab')
        root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as folder:
            previous = command_gate.MODE
            command_gate.MODE = Path(folder) / 'manual'
            fake = SimpleNamespace(pub=Publisher(), mode='auto', inputs={'auto': (0.,0.,0.), 'manual': (0.,0.,0.)},
                                   last_status=None, get_logger=lambda: SimpleNamespace(info=lambda msg: None))
            try:
                auto = Twist(); auto.linear.x = .2
                command_gate.Gate.receive(fake, 'auto', auto)
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, .2)
                command_gate.MODE.touch()
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
                command_gate.Gate.receive(fake, 'auto', auto)
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
                manual = Twist(); manual.linear.x = .1
                command_gate.Gate.receive(fake, 'manual', manual)
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, .1)
                fake.inputs['manual'] = (.1, 0., time.monotonic() - .5)
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
            finally:
                command_gate.MODE = previous

    def test_health_check_recovers_from_lost_response(self):
        from concurrent.futures import Future
        lost, replacement = Future(), Future()
        removed = []
        client = SimpleNamespace(service_is_ready=lambda: True,
                                 remove_pending_request=removed.append,
                                 call_async=lambda request: replacement)
        fake = SimpleNamespace(state_clients={'collision_monitor': client},
                               pending={'collision_monitor': (lost, time.monotonic()-1)},
                               record=lambda *args: None)
        controller_bridge.Bridge.check_states(fake)
        self.assertTrue(lost.cancelled())
        self.assertEqual(removed, [lost])
        self.assertIs(fake.pending['collision_monitor'][0], replacement)

    def test_circular_footprint_and_wheel_envelope(self):
        points = circle(.15)
        for a, b in zip(points, points[1:] + points[:1]):
            ax, ay = a[0]+.03, a[1]
            bx, by = b[0]+.03, b[1]
            distance = abs(ax*by-ay*bx) / math.hypot(bx-ax, by-ay)
            self.assertGreaterEqual(distance, .15 - 1e-6)
        self.assertLess(math.hypot(.03+.05, .22/2+.025/2), .15)


if __name__ == '__main__':
    unittest.main()


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


## tools/command_gate.py

"""Select exactly one launcher command source before Collision Monitor."""
import math
from pathlib import Path
import time
import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node

MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')


class Gate(Node):
    def __init__(self):
        super().__init__('vacuum_command_gate')
        self.pub = self.create_publisher(Twist, '/vacuum/selected_cmd_vel', 1)
        self.inputs = {'manual': (0., 0., 0.), 'auto': (0., 0., 0.)}
        self.mode = 'manual' if MODE.exists() else 'auto'
        self.last_status = None
        self.create_subscription(Twist, '/cmd_vel_smoothed', lambda msg: self.receive('auto', msg), 1)
        self.create_subscription(Twist, '/vacuum/manual_cmd_vel', lambda msg: self.receive('manual', msg), 1)
        self.create_timer(.05, self.tick)

    def receive(self, source, msg):
        v, w = msg.linear.x, msg.angular.z
        if not math.isfinite(v) or not math.isfinite(w):
            v, w = 0., 0.
        self.inputs[source] = (max(-.30, min(.50, v)), max(-1.2, min(1.2, w)), time.monotonic())

    def tick(self):
        mode = 'manual' if MODE.exists() else 'auto'
        if mode != self.mode:
            self.mode = mode
            # Require fresh input after every mode transition.
            self.inputs = {'manual': (0., 0., 0.), 'auto': (0., 0., 0.)}
        v, w, stamp = self.inputs[mode]
        message = Twist()
        if time.monotonic() - stamp < .3:
            message.linear.x, message.angular.z = v, w
        status = (mode, abs(message.linear.x) > .001 or abs(message.angular.z) > .001)
        if status != self.last_status:
            self.get_logger().info(f'Selected {mode}: speed={message.linear.x:.3f}, turn={message.angular.z:.3f}')
            self.last_status = status
        self.pub.publish(message)


def main():
    rclpy.init()
    node = Gate()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.pub.publish(Twist())
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()


## .lab/session.json

{"mode": "drive", "camera_rate": 60}

## .lab/processes.json

{"simulation": {"pid": 1549, "start": "71741"}, "command gate": {"pid": 1835, "start": "72625"}, "collision guard": {"pid": 1837, "start": "72625"}, "camera view": {"pid": 1945, "start": "72953"}}