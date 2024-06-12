package com.hakivvi.hackernickname.util;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.hakivvi.hackernickname.model.SerializationItem;

import java.lang.reflect.Constructor;
import java.util.HashMap;
import java.util.List;

public class ExperimentalSerializer {

    public static String serialize(SerializationItem[] serializable) {
        // todo
        return "";
    }

    public static HashMap<String, Object> deserialize(String serialized) {
        ObjectMapper mapper = new ObjectMapper();
        HashMap<String, Object> result = new HashMap<String, Object>();
        try {
            List<SerializationItem> dataList = mapper.readValue(serialized, new TypeReference<List<SerializationItem>>() {});
            for (SerializationItem item : dataList) {
                switch (item.type) {
                    case "string" -> result.put(item.name, item.value);
                    case "boolean" -> result.put(item.name, Boolean.valueOf(item.value));
                    case "integer" -> {
                        try {
                            Integer r = Integer.valueOf(item.value);
                            result.put(item.name, r);
                        } catch (NumberFormatException e) {
                            result.put(item.name, Integer.valueOf("0"));
                        }
                    }
                    case "double" -> {
                        try {
                            Double r = Double.valueOf(item.value);
                            result.put(item.name, r);
                        } catch (NumberFormatException e) {
                            result.put(item.name, Double.valueOf("0"));
                        }
                    }
                    case "float" -> {
                        try {
                            Float r = Float.valueOf(item.value);
                            result.put(item.name, r);
                        } catch (NumberFormatException e) {
                            result.put(item.name, Float.valueOf("0"));
                        }
                    }
                    case "long" -> {
                        try {
                            Long r = Long.valueOf(item.value);
                            result.put(item.name, r);
                        } catch (NumberFormatException e) {
                            result.put(item.name, Long.valueOf("0"));
                        }
                    }
                    case "byte" -> {
                        try {
                            Byte r = Byte.valueOf(item.value);
                            result.put(item.name, r);
                        } catch (NumberFormatException e) {
                            result.put(item.name, Byte.valueOf("0"));
                        }
                    }
                    case "object" -> {
                        try {
                            String[] args = item.value.split("\\|");
                            if (args.length == 2) {
                                Class<?> clazz = Class.forName(args[0]);
                                Constructor<?> constructor = clazz.getConstructor(String.class);
                                Object instance = constructor.newInstance(args[1]);
                                result.put(item.name, instance);
                            } else if (args.length == 3) {
                                Class<?> clazz = Class.forName(args[0]);
                                Constructor<?> constructor = clazz.getConstructor(String.class, String.class);
                                Object instance = constructor.newInstance(args[1], args[2]);
                                result.put(item.name, instance);
                            } else {
                                result.put(item.name, "Error: currently only <= 2 arguments are supported.");
                            }
                        } catch (Exception e) {
                            result.put(item.name, null);
                        }
                    }
                }
            }
            return result;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return (result);
        }
    }
}
