add_executable(AVP "")

include_directories("${INCLUDE_DIR}")

IF (WIN32)
    add_definitions(-D_WIN32_WINNT=0x0501)
ENDIF()

add_definitions(-DNOMINMAX)
add_definitions(-DUNICODE)
add_definitions(-D_UNICODE)

IF (MSVC)
    string(REPLACE "/MDd" "/MD" CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
ENDIF()

include_directories(${CMAKE_CURRENT_LIST_DIR}/eigen/3.2.3/include/eigen3)
file(GLOB_RECURSE srcs *.h *.hh *i *.hpp *.c *.cc *.cpp)
target_sources(AVP PRIVATE ${srcs})
source_group(TREE ${CMAKE_CURRENT_LIST_DIR} FILES ${srcs})

SetDefaultTargetProperties(AVP)

IF (WIN32)
    target_link_libraries(AVP  ${LIB_DIR}/SimOneIOAPI.lib ${LIB_DIR}/SSD.lib ${LIB_DIR}/HDMapModule.lib  ${LIB_DIR}/ProtobufModule.lib)

    add_custom_command(TARGET AVP
        POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${LIB_DIR}/SimOneIOAPI.dll ${BINARY_OUT_PATH}/SimOneIOAPI.dll
        COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${LIB_DIR}/SSD.dll ${BINARY_OUT_PATH}/SSD.dll
        COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${LIB_DIR}/HDMapModule.dll ${BINARY_OUT_PATH}/HDMapModule.dll
        )
ELSEIF (UNIX)
        target_link_libraries(AVP debug ${LIB_DIR}/libSimOneIOAPI.so)
        target_link_libraries(AVP optimized ${LIB_DIR}/libSimOneIOAPI.so -lpthread)
        target_link_libraries(AVP debug ${LIB_DIR}/libSSD.so)
        target_link_libraries(AVP optimized ${LIB_DIR}/libSSD.so -lpthread)
        target_link_libraries(AVP debug ${LIB_DIR}/libHDMapModule.so)
        target_link_libraries(AVP optimized ${LIB_DIR}/libHDMapModule.so)

        add_custom_command(TARGET AVP
        POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${LIB_DIR}/libSimOneIOAPI.so ${BINARY_OUT_PATH}/libSimOneIOAPI.so
        COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${LIB_DIR}/libSSD.so ${BINARY_OUT_PATH}/libSSD.so
        COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${LIB_DIR}/libHDMapModule.so ${BINARY_OUT_PATH}/libHDMapModule.so
        )
ENDIF()
