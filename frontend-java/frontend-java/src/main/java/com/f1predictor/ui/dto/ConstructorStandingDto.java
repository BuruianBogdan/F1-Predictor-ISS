package com.f1predictor.ui.dto;

public class ConstructorStandingDto {
    private Integer position;
    private Integer constructor_id;
    private String constructor_name;
    private String nationality;
    private Double points;

    public Integer getPosition() { return position; }
    public void setPosition(Integer position) { this.position = position; }

    public Integer getConstructor_id() { return constructor_id; }
    public void setConstructor_id(Integer constructor_id) { this.constructor_id = constructor_id; }

    public String getConstructor_name() { return constructor_name; }
    public void setConstructor_name(String constructor_name) { this.constructor_name = constructor_name; }

    public String getNationality() { return nationality; }
    public void setNationality(String nationality) { this.nationality = nationality; }

    public Double getPoints() { return points; }
    public void setPoints(Double points) { this.points = points; }
}