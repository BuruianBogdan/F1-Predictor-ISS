package com.f1predictor.ui.dto;

public class ResultDto {
    private Integer result_id;
    private Integer race_id;
    private Integer driver_id;
    private Integer constructor_id;
    private Integer grid;
    private Integer position;
    private Double points;
    private String status;

    public Integer getResult_id() { return result_id; }
    public void setResult_id(Integer result_id) { this.result_id = result_id; }

    public Integer getRace_id() { return race_id; }
    public void setRace_id(Integer race_id) { this.race_id = race_id; }

    public Integer getDriver_id() { return driver_id; }
    public void setDriver_id(Integer driver_id) { this.driver_id = driver_id; }

    public Integer getConstructor_id() { return constructor_id; }
    public void setConstructor_id(Integer constructor_id) { this.constructor_id = constructor_id; }

    public Integer getGrid() { return grid; }
    public void setGrid(Integer grid) { this.grid = grid; }

    public Integer getPosition() { return position; }
    public void setPosition(Integer position) { this.position = position; }

    public Double getPoints() { return points; }
    public void setPoints(Double points) { this.points = points; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
