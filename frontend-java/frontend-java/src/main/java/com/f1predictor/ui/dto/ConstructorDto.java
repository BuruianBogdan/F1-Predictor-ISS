package com.f1predictor.ui.dto;

public class ConstructorDto {
    private Integer constructor_id;
    private String constructor_ref;
    private String name;
    private String nationality;

    public Integer getConstructor_id() { return constructor_id; }
    public void setConstructor_id(Integer constructor_id) { this.constructor_id = constructor_id; }

    public String getConstructor_ref() { return constructor_ref; }
    public void setConstructor_ref(String constructor_ref) { this.constructor_ref = constructor_ref; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getNationality() { return nationality; }
    public void setNationality(String nationality) { this.nationality = nationality; }
}