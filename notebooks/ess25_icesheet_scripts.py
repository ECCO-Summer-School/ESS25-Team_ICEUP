import os
import numpy as np

def read_ecco_runoff_file(file_path, llc=90, printing=False):

    if printing:
        print('      - Reading from '+file_name)

    timesteps = 12
    grid_array = np.fromfile(file_path, '>f4')
    N = 13 * llc * llc

    runoff_faces = {}

    for i in range(1, 6):
        if i < 3:
            face_grid = np.zeros((timesteps, 3 * llc, llc))
        elif i == 3:
            face_grid = np.zeros((timesteps, llc, llc))
        if i > 3:
            face_grid = np.zeros((timesteps, llc, 3 * llc))
        runoff_faces[i] = face_grid

    for nr in range(timesteps):
        points_counted = 0
        level_grid = grid_array[nr * N:(nr + 1) * N]
        for i in range(1, 6):
            if i < 3:
                n_points = 3 * llc * llc
                grid = level_grid[points_counted:points_counted + n_points]
                grid = np.reshape(grid, (3 * llc, llc))
            if i == 3:
                n_points = llc * llc
                grid = level_grid[points_counted:points_counted + n_points]
                grid = np.reshape(grid, (llc, llc))
            if i > 3:
                n_points = 3 * llc * llc
                grid = level_grid[points_counted:points_counted + n_points]
                grid = np.reshape(grid, (llc, 3 * llc))
            runoff_faces[i][nr, :, :] = grid

            points_counted += n_points

    runoff_tiles = {}
    runoff_tiles[0] = runoff_faces[1][:,:llc,:]
    runoff_tiles[1] = runoff_faces[1][:,llc:llc*2,:]
    runoff_tiles[2] = runoff_faces[1][:,2*llc:,:]
    runoff_tiles[3] = runoff_faces[2][:,:llc,:]
    runoff_tiles[4] = runoff_faces[2][:,llc:llc*2,:]
    runoff_tiles[5] = runoff_faces[2][:,2*llc:,:]
    runoff_tiles[6] = runoff_faces[3]
    runoff_tiles[7] = runoff_faces[4][:,:, :llc]
    runoff_tiles[8] = runoff_faces[4][:,:, llc:llc*2]
    runoff_tiles[9] = runoff_faces[4][:,:, llc*2:]
    runoff_tiles[10] = runoff_faces[5][:,:, :llc]
    runoff_tiles[11] = runoff_faces[5][:,:, llc:llc*2]
    runoff_tiles[12] = runoff_faces[5][:,:, llc*2:]

    return(runoff_tiles)