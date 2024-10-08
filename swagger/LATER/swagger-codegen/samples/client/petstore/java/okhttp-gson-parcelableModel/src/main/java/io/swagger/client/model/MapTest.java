/*
 * Swagger Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * OpenAPI spec version: 1.0.0
 * Contact: apiteam@swagger.io
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import android.os.Parcelable;
import android.os.Parcel;
/**
 * MapTest
 */


public class MapTest implements Parcelable {
  @SerializedName("map_map_of_string")
  private Map<String, Map<String, String>> mapMapOfString = null;

  /**
   * Gets or Sets inner
   */
  @JsonAdapter(InnerEnum.Adapter.class)
  public enum InnerEnum {
    UPPER("UPPER"),
    LOWER("lower");

    private String value;

    InnerEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static InnerEnum fromValue(String input) {
      for (InnerEnum b : InnerEnum.values()) {
        if (b.value.equals(input)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<InnerEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final InnerEnum enumeration) throws IOException {
        jsonWriter.value(String.valueOf(enumeration.getValue()));
      }

      @Override
      public InnerEnum read(final JsonReader jsonReader) throws IOException {
        Object value = jsonReader.nextString();
        return InnerEnum.fromValue((String)(value));
      }
    }
  }  @SerializedName("map_of_enum_string")
  private Map<String, InnerEnum> mapOfEnumString = null;

  public MapTest() {
  }
  public MapTest mapMapOfString(Map<String, Map<String, String>> mapMapOfString) {
    this.mapMapOfString = mapMapOfString;
    return this;
  }

  public MapTest putMapMapOfStringItem(String key, Map<String, String> mapMapOfStringItem) {
    if (this.mapMapOfString == null) {
      this.mapMapOfString = new HashMap<String, Map<String, String>>();
    }
    this.mapMapOfString.put(key, mapMapOfStringItem);
    return this;
  }

   /**
   * Get mapMapOfString
   * @return mapMapOfString
  **/
  @Schema(description = "")
  public Map<String, Map<String, String>> getMapMapOfString() {
    return mapMapOfString;
  }

  public void setMapMapOfString(Map<String, Map<String, String>> mapMapOfString) {
    this.mapMapOfString = mapMapOfString;
  }

  public MapTest mapOfEnumString(Map<String, InnerEnum> mapOfEnumString) {
    this.mapOfEnumString = mapOfEnumString;
    return this;
  }

  public MapTest putMapOfEnumStringItem(String key, InnerEnum mapOfEnumStringItem) {
    if (this.mapOfEnumString == null) {
      this.mapOfEnumString = new HashMap<String, InnerEnum>();
    }
    this.mapOfEnumString.put(key, mapOfEnumStringItem);
    return this;
  }

   /**
   * Get mapOfEnumString
   * @return mapOfEnumString
  **/
  @Schema(description = "")
  public Map<String, InnerEnum> getMapOfEnumString() {
    return mapOfEnumString;
  }

  public void setMapOfEnumString(Map<String, InnerEnum> mapOfEnumString) {
    this.mapOfEnumString = mapOfEnumString;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MapTest mapTest = (MapTest) o;
    return Objects.equals(this.mapMapOfString, mapTest.mapMapOfString) &&
        Objects.equals(this.mapOfEnumString, mapTest.mapOfEnumString);
  }

  @Override
  public int hashCode() {
    return Objects.hash(mapMapOfString, mapOfEnumString);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MapTest {\n");
    
    sb.append("    mapMapOfString: ").append(toIndentedString(mapMapOfString)).append("\n");
    sb.append("    mapOfEnumString: ").append(toIndentedString(mapOfEnumString)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public void writeToParcel(Parcel out, int flags) {
    out.writeValue(mapMapOfString);
    out.writeValue(mapOfEnumString);
  }

  MapTest(Parcel in) {
    mapMapOfString = (Map<String, Map<String, String>>)in.readValue(Map.class.getClassLoader());
    mapOfEnumString = (Map<String, InnerEnum>)in.readValue(null);
  }

  public int describeContents() {
    return 0;
  }

  public static final Parcelable.Creator<MapTest> CREATOR = new Parcelable.Creator<MapTest>() {
    public MapTest createFromParcel(Parcel in) {
      return new MapTest(in);
    }
    public MapTest[] newArray(int size) {
      return new MapTest[size];
    }
  };
}
