add_executable(AEB "")

file(GLOB_RECURSE srcs *.h *.hh *i *.hpp *.c *.cc *.cpp *.py)
file(GLOB_RECURSE headers *.h)

target_sources(AEB PRIVATE "src/AEBSample.cpp" ${headers})

source_group(TREE ${CMAKE_CURRENT_LIST_DIR} FILES ${srcs})

include_directories("${INCLUDE_DIR}")

add_definitions(-DNOMINMAX)
add_definitions(-DUNICODE)
add_definitions(-D_UNICODE)

SetDefaultTargetProperties(AEB)


target_link_libraries(AEB debug ${LIB_DIR}/libSimOneIOAPI.so)
target_link_libraries(AEB optimized ${LIB_DIR}/libSimOneIOAPI.so -lpthread)
target_link_libraries(AEB debug ${LIB_DIR}/libSSD.so)
target_link_libraries(AEB optimized ${LIB_DIR}/libSSD.so -lpthread)
target_link_libraries(AEB debug ${LIB_DIR}/libHDMapModule.so)
target_link_libraries(AEB optimized ${LIB_DIR}/libHDMapModule.so)

add_custom_command(TARGET AEB
    POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${LIB_DIR}/libSimOneIOAPI.so ${BINARY_OUT_PATH}/libSimOneIOAPI.so
    COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${LIB_DIR}/libSSD.so ${BINARY_OUT_PATH}/libSSD.so
    COMMAND ${CMAKE_COMMAND} -E copy_if_different  ${LIB_DIR}/libHDMapModule.so ${BINARY_OUT_PATH}/libHDMapModule.so
    )
