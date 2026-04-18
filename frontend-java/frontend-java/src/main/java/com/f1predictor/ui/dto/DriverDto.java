package com.f1predictor.ui.dto;

public class DriverDto {
    private Integer driver_id;
    private String driver_ref;
    private Integer number;
    private String code;
    private String forename;
    private String surname;
    private String dob;
    private String nationality;

    public Integer getDriver_id() { return driver_id; }
    public void setDriver_id(Integer driver_id) { this.driver_id = driver_id; }

    public String getDriver_ref() { return driver_ref; }
    public void setDriver_ref(String driver_ref) { this.driver_ref = driver_ref; }

    public Integer getNumber() { return number; }
    public void setNumber(Integer number) { this.number = number; }

    public String getCode() { return code; }
    public void setCode(String code) { this.code = code; }

    public String getForename() { return forename; }
    public void setForename(String forename) { this.forename = forename; }

    public String getSurname() { return surname; }
    public void setSurname(String surname) { this.surname = surname; }

    public String getDob() { return dob; }
    public void setDob(String dob) { this.dob = dob; }

    public String getNationality() { return nationality; }
    public void setNationality(String nationality) { this.nationality = nationality; }

    public String getFullName() {
        String f = forename != null ? forename : "";
        String s = surname != null ? surname : "";
        return (f + " " + s).trim();
    }
}